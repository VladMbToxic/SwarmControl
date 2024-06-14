from swarmsys import *
from ThreeDTool import Points

rot_point = np.array([40, 0, 0])
zero_point = np.array([0, 0, 0])
p = Points([rot_point, zero_point], text=True)
arrs = []
for i in range(8):
    arrs.append(Darray())
for j, arr in enumerate(arrs):
    arr.create_square_array(center_point=np.array([0, 0, 0]))
    arr.rot_z(np.pi/4*j, rot_point=rot_point, apply=True)

dp = Dspl(arrs + [p], qt=True)
lim_1 = -20
lim_2 = 30
dp.limits(x=[lim_1, lim_2], y=[lim_1, lim_2], z=[lim_1, lim_2])
dp.ax.title.set_text(f'Вращение массива дронов по оси z и точки {rot_point}')
dp.show()


rot_point = np.array([40, 0, 0])
zero_point = np.array([0, 0, 0])
p = Points([rot_point, zero_point], text=True)
darr = Darray()
darr.create_square_array(center_point=np.array([0, 0, 0]))
darr.rot_z(np.pi/4, rot_point=rot_point, apply=True)

dp = Dspl([darr] + [p], qt=True)
lim_1 = -20
lim_2 = 30
dp.limits(x=[lim_1, lim_2], y=[lim_1, lim_2], z=[lim_1, lim_2])
dp.ax.title.set_text(f'Вращение массива дронов по оси z и точки {rot_point}')
dp.show()

