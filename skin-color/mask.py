# from scipy.ndimage import imread
import matplotlib.pyplot as plt
import cv2
import numpy as np
from sklearn.linear_model import LogisticRegressionCV


image = cv2.imread('face.jpg')
# read complete mask image details, including alpha channel
mask = cv2.imread('face.png', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

valid_image = cv2.imread('amida.jpg')
valid_image_rgb = cv2.cvtColor(valid_image, cv2.COLOR_BGR2RGB)

# plt.imshow(image_rgb)
# plt.subplot(122)

# plt.imshow(mask)
# plt.show()


# make mask semi-transparent
# alpha channel controls how transparent the pixels are.
# mask[:, :, 3] = 0  # reduce alpha
# print(mask[:, :, 0] == 0)

# # plt.imshow(image_rgb)
# plt.imshow(mask)
# plt.show()



# apply a mask on our image and retrieve all pixels the mask says is skin
skincolors = image_rgb[mask[:,:,0]==255]

# print(skincolors.shape)
# (13636, 3)

# retrieve pixel co-ords that mask says is not skin
# mask[:,:,0]==0 means all pixels where the alpha channel is 0
# [:,:,0] - width, height, channel
nonskincolors = image_rgb[mask[:,:,0]==0]

# print(skincolors)

# plt.imshow(skincolors)
# plt.imshow(nonskincolors)
# plt.show()




# # plot a scatter plot of skin and non-skin pixels
# skin_sample = skincolors[np.random.choice(len(skincolors), 500, replace=False)]
# nonskin_sample = nonskincolors[np.random.choice(len(nonskincolors), 500, replace=False)]

# plt.scatter(skin_sample[:,0], skin_sample[:,1], skin_sample[:,2], color='red', label='Skin')
# plt.scatter(nonskin_sample[:,0], nonskin_sample[:,1], nonskin_sample[:,2], color='blue', label='Non-Skin')
# plt.legend()
# plt.show()




# train a logistic regression classifier
color = np.vstack((skincolors, nonskincolors))
target = np.concatenate((np.ones(len(skincolors)),np.zeros(len(nonskincolors))))

# Split into train and test sets
learn_color = color[1::2]
test_color = color[0::2]
learn_target = target[1::2]
test_target = target[0::2]

# init and train
logregr = LogisticRegressionCV()
logregr.fit(learn_color, learn_target)

test_score = logregr.score(test_color, test_target)
print(f"Test score: {test_score}")



image_colors = valid_image_rgb.reshape((-1,3))

predict_skin = logregr.predict(image_colors).reshape(valid_image_rgb.shape[:2])

plt.subplot(121);
plt.imshow(valid_image_rgb);

plt.subplot(122);
plt.imshow(predict_skin);

plt.show();