import numpy as np

def weight_reorder_3x3(weights):
    # Split the weight matrix into 3x3 weight tiles
    weight_tiles = []
    for i in range(3):
        for j in range(3):
            weight_tiles.append(weights[:, i:i+3, j:j+3])
    
    # Reorder the weights in each tile
    reordered_tiles = []
    for tile in weight_tiles:
        rows, cols, channels = tile.shape
        reordered_tile = np.zeros((rows, cols, channels))
        for c in range(channels):
            for i in range(rows):
                for j in range(cols):
                    reordered_tile[i, j, c] = tile[i, j, c*9 + i*3 + j]
        reordered_tiles.append(reordered_tile)
    
    # Concatenate the reordered tiles to form the new weight matrix
    reordered_weights = np.concatenate([np.concatenate(reordered_tiles[:3], axis=2),
                                         np.concatenate(reordered_tiles[3:6], axis=2),
                                         np.concatenate(reordered_tiles[6:], axis=2)],
                                        axis=1)
    return reordered_weights