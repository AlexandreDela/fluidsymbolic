from fluidsymbolic.stream import StreamFuncAnim, StreamFunctionManager
import sympy.abc as spa


X = spa.r
Y = spa.s
stream_function, curl_stream = \
    StreamFunctionManager.cylinder_stream_function(
        x_sympy=X,
        y_sympy=Y,
        origin_x=1,
        origin_y=-1)
animation = StreamFuncAnim(
    X,
    Y,
    stream_function,
    ylim=(-5,5),
    xlim=(-5,5),
    curl=curl_stream,
    streamline_options={"density": 3},
    hide_latex=True
)
animation.add_circle_patch(origin= [1, -1], radius = 1.)
animation.save_animator(
    "./test.gif",
    300,
    1000
)
