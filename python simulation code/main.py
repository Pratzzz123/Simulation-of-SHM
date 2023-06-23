#The code is available to run on https://trinket.io/glowscript/297977d805
win = 500
scene = canvas(title="Physics PBL\n\n", align = 'left', width = win, height = win,
               center=vec(0, 0, 0), background=color.white)
e = 2.71828
pi = 3.14159
springLength = 0.05    # meters

m = float(input("Enter the value of mass (in kg): "))
k = float(input("Enter the value of k (in N/m): "))
zeta = float(input("Enter the value of zeta: "))
gravField = float(input("Enter the value of g (m/s^2): "))

spring = helix(pos=vec(0, 0, 0), axis=vec(0, -2*springLength, 0),
               thickness=0.0025*k, radius=0.09, color=color.white)
spring.coils = 20

table = box(pos=vec(0, 0, 0), size=vec(1.6, 0.08, 2), color=color.orange)

springLength = 0.1

phi = pi/2

wn = (k/m)**(1/2)
wd = wn*((1-(zeta**2))**(1/2))
A = m*gravField/k

bobMass = m   # kilograms
# gravField = 9.8             # Newtons per kilogram
velocity = vec(0, 0, 0)   # starts by falling from rest
bob = box(color=color.red)
bob.pos = spring.pos + spring.axis
bob.axis = vec(0, 0.002, 0)
bob.size = vec(0.3, 0.3, 0.3)

t = 0         # start time
dt = 0.01
gg = graph(align='right', width= 1.3*win, height = 0.7*win,
    xtitle='time', ytitle='displacement')
f1 = gcurve()
running = True
def Run(b): # b = button
    global running, remember_dt, dt
    running = not running
    if running:
        b.text = "Pause"
        dt = remember_dt
    else: 
        b.text = "Play"
        remember_dt = dt
        dt = 0
    return

button(text="Pause", pos=scene.title_anchor, bind=Run)
# print_options(readonly=False) #<-- for read only output results
print_options(digits=4)
scene.append_to_title("\n<b>m = </b>"+bobMass+ ", <b>k = </b>" +k+ ", <b>zeta = </b>"+zeta+", <b>g = </b>"+gravField+"\n\n")
while (True):

        rate(150)
        t = t + dt

        bob.pos = vec(0, A*(e**(-zeta*wn*t))*sin((wd*t)-phi)-(A+0.2), 0)

        spring.axis = bob.pos

        bob.axis = bob.axis.mag * (spring.pos - bob.pos).norm()

        f1.plot(t, bob.pos.y+(A+0.2))

        print(t+",", bob.pos.y+(A+0.2))
    
