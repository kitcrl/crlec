import os
import numpy as np
import math
import cv2

#img1 = 'pf_freq_d_05.00.bmp';
#img2 = 'pf_freq_d_05.00.bmp.ctus.bmp.bmp';

img1 = 'ctus.bmp';
#img2 = 'pf_freq_d_05.00.bmp.ctus.bmp.bmp';
img2 = 'pf_sin_d_05.00.bmp.ctus.bmp.bmp';


ppath = os.getcwd() + "\\imgs\\";


def psnr(img1, img2):
    mse = np.mean((img1/1. - img2/1.) ** 2 )
    if mse < 1.0e-10:
        return 100*1.0
    return 10 * math.log10(255.0*255.0/mse)

def mse(img1,img2):
    mse = np.mean((img1/1. - img2/1.) ** 2 )
    return mse

def ssim(y_true , y_pred):
    u_true = np.mean(y_true)
    u_pred = np.mean(y_pred)
    var_true = np.var(y_true)
    var_pred = np.var(y_pred)
    std_true = np.sqrt(var_true)
    std_pred = np.sqrt(var_pred)
    c1 = np.square(0.01*7)
    c2 = np.square(0.03*7)
    ssim = (2 * u_true * u_pred + c1) * (2 * std_pred * std_true + c2)
    denom = (u_true ** 2 + u_pred ** 2 + c1) * (var_pred + var_true + c2)
    return ssim / denom

list_psnr = []
list_ssim = []
list_mse = []
img_a = cv2.imread(ppath+img1)
img_b = cv2.imread(ppath+img2)
psnr_num = psnr(img_a, img_b)
ssim_num = ssim(img_a, img_b)
mse_num = mse(img_a,img_b)
list_ssim.append(ssim_num)
list_psnr.append(psnr_num)
list_mse.append(mse_num)
print("  PSNR:",np.mean(list_psnr))#,list_psnr)
print("  SSIM:",np.mean(list_ssim))#,list_ssim)
print("  MSE:",np.mean(list_mse))#,list_mse)
