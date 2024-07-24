from fluidsymbolic.stream import StreamFuncAnim, StreamFunctionManager
import sympy.abc as spa


X = spa.x
Y = spa.y
epsi = spa.epsilon
M = spa.M
stream_function, vorticity = \
    StreamFunctionManager.cylinder_stream_janzen_rayleigh_expansion(
        x_sympy=X,
        y_sympy=Y,
        epsilon_sympy=epsi,
        m_sympy=M
    )
animation = StreamFuncAnim(
    X,
    Y,
    stream_function,
    ylim=(-5,5),
    xlim=(-5,5),
    vorticity=vorticity,
    streamline_options={"density": 3},
    dict_eval={"epsilon" : (epsi, 0.1), "M": (M, 0.1)},
    suptitle="Janzen–Rayleigh expansion"
)
animation.add_circle_patch(origin= [0, 0], radius = 1.)
animation.save_animator(
    "./test.gif",
    300,
    1000
)