import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

build = ["2.16.4.1554", "2.17.0.1539", "2.17.1.1594"]
KuruFaceiOS = ["", "94", "94"]
YukiCameraToolKit = ["130", "133", "131"]
YukiLiveKit = ["", "247", "246"]
YukiLiveness = ["", "29", "29"]
Sum = ["130", "503", "500"]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(build)
        .add_yaxis("KuruFaceiOS", KuruFaceiOS)
        .add_yaxis("YukiCameraToolKit", YukiCameraToolKit)
        .add_yaxis("YukiLiveKit", YukiLiveKit)
        .add_yaxis("YukiLiveness", YukiLiveness)
        .add_yaxis("합계", Sum)
        .set_global_opts(
        title_opts=opts.TitleOpts(title="yuki SDK size: iOS", subtitle="측정단위:MB"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False
        ),
    )
        .set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            label_opts=opts.LabelOpts(position="inside", font_size=8)
        ),
        label_opts=opts.LabelOpts(is_show=True),
    )
)
line.render("아이폰 파일사이즈.html")
