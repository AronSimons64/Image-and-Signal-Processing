import numpy as np
import matplotlib.pyplot as plt

def find_peaks(a, dx = 0, h = 0, debug = False):
            """
                Finds the local maxima of an array. 

                Parameters
                ----------
                a : array_like
                    1D input array
                
                dx : int, optional
                    minimum separation of peak
                h : float, optional
                    minimum height of peak

                debug : bool, optional
                    Set True to activate debugger for this function.
                
                Returns
                ----------
                x : int
                    position of the calculated peaks with minimum separation dx and minimum height h
                y : float
                    intensity of peak at position x
            """
            # if debug == True:
            #     plt.plot(a)
            #     plt.show()
            # Normalize the data
            a = normalize(a)
            
            x = []
            y = []
            x_new = []

            # Loop over the array and check for local maxima
            for i in range(1,len(a) - 1):
                # Save the left, center, and right point
                left   = a[i - 1]
                center = a[i]
                right  = a[i + 1]

                # If the center is greater than either side, continue
                if center > left and center > right:
                    
                    if debug == True:
                        print('x-position','intensity','minimum height','condition satisfied')
                        print(i, a[i],h,a[i]>=h)

                    # If the array value is greater than h, store the position and height.
                    if a[i] >= h:
                        x.append(i)
                        y.append(a[i])
            
            # Convert to numpy array
            x = np.array(x)
            y = np.array(y)

            # If no peaks have been found, raise error
            if len(x) == 0:
                raise Exception (f"Could not find peak in given array with h = {h} and dx = {dx}.")
            
            # If minimum separation is required, enter this loop
            if dx != 0:
                loop = True
                new_pos = 0
                old_pos = -1
                
                while loop == True:
                    
                    # Check which peaks are within dx of each other
                    within_dx = np.where(x[new_pos:] - x[new_pos] < dx)[0]
                    within_dx = within_dx + new_pos
                    
                    # Find the highest peak in the given range
                    m = np.argmax(a[x[within_dx]]) 

                    if debug == True:
                        print('x-values of peak','\t','indices of x-values','\t','max value of indices','\t','length of x-array')
                        print(x[within_dx],'\t','\t', within_dx,'\t','\t', np.max(within_dx),'\t','\t', len(x))
                    
                    # Save the highest peak location as new position
                    new_pos += m

                    # If the iterations have converged, store the peak location in an array
                    if x[old_pos] == x[new_pos]:
                        if debug == True:
                            print('stored x-position of peak',x[new_pos])

                        # Save the peak to a new array
                        x_new.append(x[new_pos])

                        # Reset the new position to one larger than the stored position
                        new_pos = np.max(within_dx) + 1

                    # If the end of the array is within reach, stop the loop
                    if np.max(within_dx) + 1 == len(x):
                        """ CAUTION: READ COMMENT"""
                        x_new.append(x[old_pos]) # CAUTION: When this line is enabled, sometimes code does not work --> when final peak is detected. You can turn it off when this happens.
                        
                        # Stop the loop
                        loop = False

                    # Reset the old position counter
                    old_pos = new_pos
            
            if len(x_new) != 0:
                x = x_new
                x = np.array(x)


            if debug == True and len(x) != 0:
                plt.plot(a,label='signal')
                for i in x:
                    plt.axvline(i,color='red')
                plt.axvline(i,color='red',label='found peaks')
                plt.legend()
                plt.show()

            x = np.unique(x)
            y = np.unique(y)
            return x,y
