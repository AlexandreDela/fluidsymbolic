from fluidsymbolic.stream import StreamFuncAnim, StreamFunctionManager
import sympy.abc as spa


X = spa.x
Y = spa.y
epsi = spa.epsilon
stream_function, vorticity = \
    StreamFunctionManager.cylinder_stream_function_porous(
        x_sympy=X,
        y_sympy=Y,
        epsilon_sympy=epsi)
animation = StreamFuncAnim(
    X,
    Y,
    stream_function,
    ylim=(-5,5),
    xlim=(-5,5),
    vorticity=vorticity,
    streamline_options={"density": 3},
    dict_eval={"epsilon" : (epsi, 0.1)}
)
animation.add_circle_patch(origin= [0, 0], radius = 1.)
animation.save_animator(
    "./test.gif",
    20,
    1000
)