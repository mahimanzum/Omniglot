# -*- coding: utf-8 -*-
"""NonEuclidean_Meta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CWi2mAghzNflS0tLhdF71g2Je2SoVE1r
"""

! git clone https://github.com/mahimanzum/non_eucliden_meta_learner.git

cd non_eucliden_meta_learner/omniglot/

ls

!pip install mctorch-lib

!python omniglot_train_one_shot.py -w 5 -s 1 -b 19

!python omniglot_non_euclidean.py -w 5 -s 1 -b 19







