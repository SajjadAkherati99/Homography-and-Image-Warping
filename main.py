import numpy as np
import cv2


def warp(im, H, out_shape):
    
    lent, wid = out_shape[0], out_shape[1]
    x = np.zeros((lent, wid, 3))
    H = np.linalg.inv(H)

    for i in range(0, lent):
        for j in range(0, wid):
            y = np.array([i, j, 1])
            transformed = np.dot(H, y.T)
            m, n = int(round(transformed[0])), int(round(transformed[1]))
            length_im, width_im = im.shape[0], im.shape[1]
            if 0 <= m < length_im and 0 <= n < width_im:
                x[i, j, :] = im[m, n, :]

    return x


image = cv2.imread('books.jpg')

# first book:
xul_S = np.array([795, 420, 1])
xur_S = np.array([667, 624, 1])
xdr_S = np.array([972, 813, 1])
xdl_S = np.array([1100, 609, 1])

width = int(np.round(0.5 * ((np.sum((xul_S - xur_S) ** 2)) ** 0.5 + (np.sum((xdl_S - xdr_S) ** 2)) ** 0.5)))
length = int(np.round(0.5 * ((np.sum((xul_S - xdl_S) ** 2)) ** 0.5 + (np.sum((xur_S - xdr_S) ** 2)) ** 0.5)))

xul_D = np.array([0, 0, 1])
xur_D = np.array([0, width, 1])
xdr_D = np.array([length, width, 1])
xdl_D = np.array([length, 0, 1])

point_S = np.array([xdr_S, xdl_S, xul_S, xur_S])
point_D = np.array([xul_D, xur_D, xdr_D, xdl_D])

h = cv2.findHomography(point_S, point_D)[0]
print("for book 'res04.jpg': h = \n", h)

out = warp(image, h, [length, width])
cv2.imwrite('res04.jpg', out)

# second book:
xul_S = np.array([103, 382, 1])
xur_S = np.array([207, 667, 1])
xdr_S = np.array([401, 600, 1])
xdl_S = np.array([297, 315, 1])

length = int(np.round(0.5 * ((np.sum((xul_S - xur_S) ** 2)) ** 0.5 + (np.sum((xdl_S - xdr_S) ** 2)) ** 0.5)))
width = int(np.round(0.5 * ((np.sum((xul_S - xdl_S) ** 2)) ** 0.5 + (np.sum((xur_S - xdr_S) ** 2)) ** 0.5)))

xul_D = np.array([0, 0, 1])
xur_D = np.array([0, width, 1])
xdr_D = np.array([length, width, 1])
xdl_D = np.array([length, 0, 1])

point_S = np.array([xur_S, xdr_S, xdl_S, xul_S])
point_D = np.array([xul_D, xur_D, xdr_D, xdl_D])

h = cv2.findHomography(point_S, point_D)[0]
print("\n\nfor book 'res05.jpg': h = \n", h)

out = warp(image, h, [length, width])
cv2.imwrite('res05.jpg', out)

# third book:
xul_S = np.array([427, 204, 1])
xur_S = np.array([464, 404, 1])
xdr_S = np.array([741, 351, 1])
xdl_S = np.array([704, 151, 1])

width = int(np.round(0.5 * ((np.sum((xul_S - xur_S) ** 2)) ** 0.5 + (np.sum((xdl_S - xdr_S) ** 2)) ** 0.5)))
length = int(np.round(0.5 * ((np.sum((xul_S - xdl_S) ** 2)) ** 0.5 + (np.sum((xur_S - xdr_S) ** 2)) ** 0.5)))

xul_D = np.array([0, 0, 1])
xur_D = np.array([0, width, 1])
xdr_D = np.array([length, width, 1])
xdl_D = np.array([length, 0, 1])

point_S = np.array([xdr_S, xdl_S, xul_S, xur_S])
point_D = np.array([xul_D, xur_D, xdr_D, xdl_D])

h = cv2.findHomography(point_S, point_D)[0]
print("\n\nfor book 'res06.jpg': h = \n", h)

out = warp(image, h, [length, width])
cv2.imwrite('res06.jpg', out)
