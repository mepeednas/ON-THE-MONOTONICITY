#This program determines the Fourier coefficients of dim 2 Victor Miller basis elements and displays them as result
Delta = delta_qexp(7) # this means you are taking Fourier expansion up to an absolute precision of O(q^7)
#eisenstein_series_qexp(k, 6) weight k arithmetically normalised Eisenstein Series upto order 6 (so that a(1)= 1, but we lose a(0)=1)
E6 = -504*eisenstein_series_qexp(6, 7)
E4 = 240*eisenstein_series_qexp(4, 7)
#k=24
print(f"This program determines the Fourier coefficients of all dimension 2 Victor Miller basis elements and displays them as result\n")
print(f"k=24")
print(f"The Fourier expansion of Delta^2 is = {Delta^2}\n\n and that of Delta*E_6^2 = {Delta*E6^2}\n\n\n\n")
#k=28
print(f"k=28")
print(f"The Fourier expansion of Delta^2 E_4 is = {Delta^2*E4}\n\n and that of Delta E_6^2 E_4= {Delta*E6^2*E4}\n\n\n\n")
#k=30
print(f"k=30")
print(f"The Fourier expansion of Delta^2 E_6 is = {Delta^2*E6}\n\n and that of Delta*E_6^3 = {Delta*E6^3}\n\n\n\n")
#k=32
print(f"k=32")
print(f"The Fourier expansion of Delta^2 E_4^2 is = {Delta^2*E4^2}\n\n and that of Delta E_6^2 E_4^2= {Delta*E6^2*E4^2}\n\n\n\n")
#k=34
print(f"k=34")
print(f"The Fourier expansion of Delta^2 E_4 E_6 is = {Delta^2*E4*E6}\n\n and that of Delta E_6^3 E_4= {Delta*E6^3*E4}\n\n\n\n")
#k=38
print(f"k=38")
print(f"The Fourier expansion of Delta^2 E_4^2 E_6 is = {Delta^2*E4^2*E6}\n\n and that of Delta E_6^3 E_4^2= {Delta*E6^3*E4^2}\n\n\n\n")
