from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="PicMenu",
    description="为已安装的插件提供可视化的帮助菜单",
    usage="显示所有插件及描述：菜单\n"
    "显示某一插件的功能菜单：菜单 插件名/序号\n"
    "显示某一功能详情：菜单 插件名/序号 功能名/序号\n"
    "注：插件名/功能名 支持模糊匹配",
    type='application',
    homepage='https://github.com/hamo-reid/nonebot_plugin_PicMenu',
    extra={
        "author": "hamo-reid",
        "menu_data": [
            {
                "func": "查询菜单",
                "trigger_method": "命令：菜单",
                "trigger_condition": "开头匹配[Any]",
                "brief_des": "用于查询本插件的各级菜单",
                "detail_des": "查看插件总表、插件命令和命令详情,具体方法如下：\n"
                "查看菜单总表：菜单\n"
                "查看插件命令：菜单 插件名/编号\n"
                "查看命令详情：菜单 插件名/编号 命令/命令编号\n"
                "插件名和命令均支持模糊查找",
            },
        ],
        "menu_template": "default",
    },
)
