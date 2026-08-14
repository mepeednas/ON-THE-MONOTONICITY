#This program determines the Fourier coefficients of all Victor Miller basis elements within dimension 3 space of cusp forms and displays them as result

print(f"This program determines the first few Fourier coefficients of all Victor Miller basis elements within dimension 3 space of cusp forms and displays them as result\n")

Delta = delta_qexp(7) # this means you are taking Fourier expansion upto order 6
#eisenstein_series_qexp(k, 6) weight k arithmetically normalised Eisenstein Series upto order 6 (so that a(1)= 1, but we lose a(0)=1)
E6 = -504*eisenstein_series_qexp(6, 7)
E4 = 240*eisenstein_series_qexp(4, 7)
#k=36
print(f"k=36")
print(f"The Fourier expansion of Delta^3 is = {Delta^3},\n\n Delta^2 E_6^2 is = {Delta^2*E6^2},\n\n and that of Delta*E6^4 is = {Delta*E6^4}\n\n\n\n")
#k=40
print(f"k=40")
print(f"The Fourier expansion of Delta^3*E4 is = {Delta^3*E4},\n\n Delta^2*E6^2*E4 is = {Delta^2*E6^2*E4},\n\n and that of Delta*E6^4*E4 is = {Delta*E6^4*E4}\n\n\n\n")
#k=42
print(f"k=42")
print(f"The Fourier expansion of Delta^3*E6 is = {Delta^3*E6},\n\n Delta^2*E6^3 is = {Delta^2*E6^3},\n\n and that of Delta*E6^5 is = {Delta*E6^5}\n\n\n\n")
#k=44
print(f"k=44")
print(f"The Fourier expansion of Delta^3*E4^2 is = {Delta^3*E4^2},\n\n Delta^2*E6^2*E4^2 is = {Delta^2*E6^2*E4^2},\n\n and that of Delta*E6^4*E4^2 is = {Delta*E6^4*E4^2}\n\n\n\n")
#k=46
print(f"k=46")
print(f"The Fourier expansion of Delta^3*E6*E4 is = {Delta^3*E6*E4},\n\n Delta^2*E6^3*E4 is = {Delta^2*E6^3*E4},\n\n and that of Delta*E6^5*E4 is = {Delta*E6^5*E4}\n\n\n\n")
#k=50
print(f"k=50")
print(f"The Fourier expansion of Delta^3*E6*E4^2 is = {Delta^3*E6*E4^2},\n\n Delta^2*E6^3*E4^2 is = {Delta^2*E6^3*E4^2},\n\n and that of Delta*E6^5*E4^2 is = {Delta*E6^5*E4^2}\n\n\n\n")
