from fluidsymbolic.stream import StreamFuncAnim, StreamFunctionManager
import sympy.abc as spa

X = spa.x
Y = spa.y
stream_function, curl_stream = \
    StreamFunctionManager.cylinder_stream_function(
        x_sympy=X,
        y_sympy=Y)
animation = StreamFuncAnim(
    X,
    Y,
    stream_function,
    ylim=(-5,5),
    xlim=(-5,5)
)
animation.add_circle_patch(origin= [0, 0], radius = 1.)
animation.save_animator(
    "./test.gif",
    300,
    1000
)
