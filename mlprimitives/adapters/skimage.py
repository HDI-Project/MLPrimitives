# -*- coding: utf-8 -*-

import skimage

from mlprimitives.utils import image_transform


def hog(X, image_shape, orientations, pixels_per_cell_x, pixels_per_cell_y,
        cells_per_block_x, cells_per_block_y, block_norm, visualize, multichannel):

    return image_transform(
        skimage.feature.hog,
        reshape_before=True,
        image_shape=image_shape,
        pixels_per_cell=(pixels_per_cell_x, pixels_per_cell_y),
        cells_per_block=(cells_per_block_x, cells_per_block_y),
        block_norm=block_norm,
        visualize=visualize,
        multichannel=multichannel
    )
