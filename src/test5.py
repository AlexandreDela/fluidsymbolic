from fluidsymbolic.stream import StreamFuncAnim, StreamFunctionManager
import sympy.abc as spa


X = spa.x
Y = spa.y
epsi = spa.epsilon
chi = spa.chi
stream_function, vorticity = \
    StreamFunctionManager.cylinder_stream_function_slight_vorticity_parabolic_shear(
        x_sympy=X,
        y_sympy=Y,
        epsilon_sympy=epsi,
        chi_sympy=chi
    )
animation = StreamFuncAnim(
    X,
    Y,
    stream_function,
    ylim=(-5,5),
    xlim=(-5,5),
    vorticity=vorticity,
    streamline_options={"density": 3},
    dict_eval={"epsilon" : (epsi, 0.1), "chi": (chi, 0.2)},
    suptitle="Parabolic Shear with Vorticity"
)
animation.add_circle_patch(origin= [0, 0], radius = 1.)
animation.save_animator(
    "./test.gif",
    20,
    1000
)