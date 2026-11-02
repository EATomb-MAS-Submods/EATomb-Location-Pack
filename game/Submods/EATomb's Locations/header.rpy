# 注册子模组
init -990 python:
    store.mas_submod_utils.Submod(
        author="EATomb",
        name="EATomb的房间包",
        description="这个子模组添加了由EATomb制作的所有房间, 目前正在持续更新中.",
        version="1.1.0"
    )

# 注册子模组更新器
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="EATomb的房间包",
            user_name="EATomb-MAS-Submods",
            repository_name="EATomb-Location-Pack",
            update_dir="",
            attachment_id=None
        )