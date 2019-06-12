import numpy as np
import sys
import config
import func

np.set_printoptions(threshold=sys.maxsize)

data = np.load('arr4.npy')

inputs = data[:, len(config.themes):]
labels = data[:, :len(config.themes)]

poem = 'How do I love thee? Let me count the ways. I love thee to the depth and breadth and height My soul can reach, when feeling out of sight For the ends of being and ideal grace. I love thee to the level of every day’s Most quiet need, by sun and candle-light. I love thee freely, as men strive for right. I love thee purely, as they turn from praise. I love thee with the passion put to use In my old griefs, and with my childhood’s faith. I love thee with a love I seemed to lose With my lost saints. I love thee with the breath, Smiles, tears, of all my life; and, if God choose, I shall but love thee better after death.'

poem = func.process_poem(poem, False)

print(len(func.convert_poem_binary(config.max_characters, poem)))
