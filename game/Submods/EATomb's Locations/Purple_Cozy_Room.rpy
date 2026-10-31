###====================================================
### Purple Cozy Room
## NOTE: Basic Materials
#      Room:
#          https://unsplash.com/photos/cozy-bedroom-with-bed-window-and-hanging-plants-rS0d3l1YRgI
#          and
#          https://unsplash.com/photos/cozy-bedroom-with-artistic-decoration-and-plants--H9PHALS2xU
#       By POOJAN THANEKAR: https://unsplash.com/@poojanclicks
#
#      Table Texture:
#          https://unsplash.com/photos/a-close-up-of-a-marble-textured-surface-8GUOLtII7ig
#       By Akbar Nemati: https://unsplash.com/@akbarnemati

# Thanks POOJAN THANEKAR and Akbar Nemati, these pictures are very nice.
###====================================================

###START: IMAGE DEFINITIONS
image purple_cozy_room_day = "mod_assets/location/Purple Cozy Room/pcr.png"
image purple_cozy_room_rain = "mod_assets/location/Purple Cozy Room/pcr_rain.png"
image purple_cozy_room_overcast = "mod_assets/location/Purple Cozy Room/pcr_overcast.png"
image purple_cozy_room_snow = "mod_assets/location/Purple Cozy Room/pcr_snow.png"

#Night images
image purple_cozy_room_night = "mod_assets/location/Purple Cozy Room/pcr-n.png"
image purple_cozy_room_rain_night = "mod_assets/location/Purple Cozy Room/pcr_rain-n.png"
image purple_cozy_room_overcast_night = "mod_assets/location/Purple Cozy Room/pcr_overcast-n.png"
image purple_cozy_room_snow_night = "mod_assets/location/Purple Cozy Room/pcr_snow-n.png"

#Sunset images
image purple_cozy_room_ss = "mod_assets/location/Purple Cozy Room/pcr-ss.png"
image purple_cozy_room_rain_ss = "mod_assets/location/Purple Cozy Room/pcr_rain-ss.png"
image purple_cozy_room_overcast_ss = "mod_assets/location/Purple Cozy Room/pcr_overcast-ss.png"
image purple_cozy_room_snow_ss = "mod_assets/location/Purple Cozy Room/pcr_snow-ss.png"


init -1 python:
    purple_cozy_room = MASFilterableBackground(
        # ID
        "purple_cozy_room",
        "温暖的粉紫色休息室",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "purple_cozy_room_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "purple_cozy_room_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "purple_cozy_room_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "purple_cozy_room_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "purple_cozy_room_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "purple_cozy_room_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "purple_cozy_room_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "purple_cozy_room_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "purple_cozy_room_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "purple_cozy_room_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "purple_cozy_room_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "purple_cozy_room_snow_ss",
            }),
        ),

        #NOTE: YOU DO NOT NEED TO TOUCH THIS
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        #FOR BACKGROUND PROPERTIES (DON'T TOUCH "ENTRY_PP:/EXIT_PP:)
        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=True,
        entry_pp=store.mas_background._purple_cozy_room_entry,
        exit_pp=store.mas_background._purple_cozy_room_exit,
        ex_props={"skip_outro": None}
    )

# 重新定义配套nou背景命名
init 100 python in mas_cardgames:
    DESK_SPRITES_MAP["purple_cozy_room"] = MASFilterSwitch(
        "mod_assets/games/nou/desks/pcr_black_marble.png"
    )

default pcr_table_other = "方形"

init -2 python in mas_background:
    PCR_TABLE_ROUND = "pcr_round"
    # PCR_TABLE_SQUARE = "pcr_square"

    # def pcr_switch_table():
    #     if store.monika_chr.tablechair.table == PCR_TABLE_ROUND:
    #         store.monika_chr.tablechair.table = PCR_TABLE_SQUARE
    #         store.pcr_table_other = "圆形"
    #     else:
    #         store.monika_chr.tablechair.table = PCR_TABLE_ROUND
    #         store.pcr_table_other = "方形"


    def _purple_cozy_room_entry(_old, **kwargs):
        """
        Entry programming point for purple_cozy_room background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("purple_cozy_room_switch_dlg"):
                store.pushEvent("purple_cozy_room_switch_dlg")

        store.monika_chr.tablechair.table = PCR_TABLE_ROUND
        store.monika_chr.tablechair.chair = "PCR"

        # TODO: 进入pcr后解锁换桌子话题
        # store.mas_unlockEVL("tomb_pcr_change_table", "EVE")

        store.pcr_table_other = (
        "方形" if store.monika_chr.tablechair.table == PCR_TABLE_ROUND else "圆形"
    )

    def _purple_cozy_room_exit(_new, **kwargs):
        """
        Exit programming point for purple_cozy_room background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

        # TODO: 离开pcr后锁上换桌子话题
        # store.mas_lockEVL("tomb_pcr_change_table", "EVE")


label purple_cozy_room_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "喜欢这种氛围的房间吗, [player]?",
            "待在这感觉会变困呢...哈哈!",
            "我们在这休息一下吧~",
            "还有圆形的窗户呢~"
        ]))

    m 3hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "那儿真不错, 对吧?",
            "我们下回再去一趟吧.",
        ]))

    m 1hua "[switch_quip]"
    return


# # TODO: 询问player是否更换桌子
# init 5 python:
#     addEvent(
#         Event(
#             persistent.event_database,
#             eventlabel="tomb_pcr_change_table",
#             category=["地点"],
#             prompt="你可以换张[pcr_table_other]的桌子吗?",
#             pool=True,
#             unlocked=False,
#             rules={"no_unlock": None},
#             aff_range=(mas_aff.ENAMORED, None)
#         ),
#     )

# label tomb_pcr_change_table:
#     m 1eub "好啊, [player]."
#     m 1hua "稍微等一下哦~"

#     show monika 1hua at lhide
#     pause 0.8
#     hide monika

#     $ store.mas_background.pcr_switch_table()

#     show monika 1eua at ls32 zorder MAS_MONIKA_Z

#     m 3hub "好啦!"
#     return

