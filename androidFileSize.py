import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

build = ["2.16.4.1554", "2.17.0.1539", "2.17.1.1588"]
sum = ["110.1", "120.3", "109.3"]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(xaxis_data=build)
        .add_yaxis("합계", sum)
        .set_global_opts(
        title_opts=opts.TitleOpts(title="yuki SDK size: Android", subtitle="측정단위:MB"),
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
        ),
    )
)
line.render("안드로이드 파일사이즈.html")