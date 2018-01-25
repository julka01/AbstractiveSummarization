# Script used to translate the raw tokenized text sources to word vectors using an existing vector vocabulary

import gensim.models as gm
import numpy as np
import os


VECTORS_SOURCE = "vectors/cnn_dm_vectors_100_5_5"

CNN_SOURCE = "C:\\Users\\Nicolas\\Desktop\\NLP Data\\cnn-dailymail-master\\cnn_stories_tokenized"
DM_SOURCE = "C:\\Users\\Nicolas\\Documents\\Passau\\Text Mining Project\\PROJECT\\dm_stories_tokenized"

CNN_INPUT_DIR = "D:\\cnn_stories_vectorized_100"
DM_INPUT_DIR = "D:\\dm_stories_vectorized_100_"

vectors = gm.KeyedVectors.load(VECTORS_SOURCE)

cnn_dir = os.listdir(CNN_SOURCE)
for file in cnn_dir:
    is_summary = False
    raw = []
    summary = []
    source = open(os.path.join(CNN_SOURCE, file), errors="ignore")
    for line in source:
        if line == '@highlight\n':
            is_summary = True
        elif line != "\n":
            tokens = line.split(' ')
            to_fill = summary if is_summary else raw
            for token in tokens:
                if token in vectors:
                    to_fill.append(vectors[token])
    raw_array = np.array(raw)
    sum_array = np.array(raw)
    np.save(os.path.join(CNN_INPUT_DIR, file + '_raw'), raw)
    np.save(os.path.join(CNN_INPUT_DIR, file + '_sum'), summary)

print('CNN has been vectorized')

# dm_dir = os.listdir(DM_SOURCE)
# file_count = 0
# # Split the output in several directories to avoid having too many files in one place
# # Also allows to resume processing in case of failure
# quarter = len(dm_dir) / 4
# for file in dm_dir:
#     is_summary = False
#     raw = []
#     summary = []
#     source = open(os.path.join(DM_SOURCE, file), errors="ignore")
#     for line in source:
#         if line == '@highlight\n':
#             is_summary = True
#         elif line != "\n":
#             tokens = line.split(' ')
#             to_fill = summary if is_summary else raw
#             for token in tokens:
#                 if token in vectors:
#                     to_fill.append(vectors[token])
#     raw_array2 = np.array(raw)
#     sum_array2 = np.array(raw)
#     np.save(os.path.join(DM_INPUT_DIR + str(int(file_count // quarter)), file + '_raw'), raw)
#     np.save(os.path.join(DM_INPUT_DIR + str(int(file_count // quarter)), file + '_sum'), summary)
#     file_count += 1

# print('DM has been vectorized')