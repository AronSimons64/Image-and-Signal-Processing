import numpy as np
import matplotlib.pyplot as plt

def EdgeDetection(img, x1, x2, wsize = 20, debug = False):
                """
                Find the highest gradient point across the entire height from top of waveguide to bottom Q-layer.

                Parameters
                ----------

                img : array_like
                    2D array of image, grayscale

                wsize : int, optional
                    window size of smoothing function.

                Returns
                ---------
                
                edge : 1D array
                detected edge
     
                """

                H,W = img.shape
                
                edge = []
                for y in range(y_top,y_bottom):
                    I = img[y,x1:x2]
                    I = CosineSmooth(I,wsize) # See CosineSmoothening.py
                    dI = abs(np.diff(I))

                    x,_ = find_peaks(dI,h=0.5) # See FindPeaks.py 
                    
                    edge.append(np.max(x))
                    

                # Remove false detections (noise)
                noise = np.where(abs(np.diff(edge)) > 4)[0]
                for i in noise:
                    edge[i] = edge[i - 1]

                if debug == True:
                    plt.title('Detected edges')
                    plt.imshow(img[:,x1:x2])
                    plt.plot(edge,np.linspace(0, H, H),color='red')
                    plt.legend()
                    plt.show()

                return edge
