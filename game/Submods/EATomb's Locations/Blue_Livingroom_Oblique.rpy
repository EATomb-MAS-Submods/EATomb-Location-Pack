###====================================================
### Blue Living Oblique
## NOTE: Basic materials from https://unsplash.com/photos/teal-living-room-with-striped-sofa-and-large-windows-bkRFra3gCEg
# The homepage of Clay banks' unsplash website: https://unsplash.com/@claybanks
# Thanks Clay Banks, his pictures are very nice.
###====================================================

###START: IMAGE DEFINITIONS
image submod_blue_livingroom_oblique_day = "mod_assets/location/Blue Livingroom(oblique)/blo.png"
image submod_blue_livingroom_oblique_rain = "mod_assets/location/Blue Livingroom(oblique)/blo_rain.png"
image submod_blue_livingroom_oblique_overcast = "mod_assets/location/Blue Livingroom(oblique)/blo_overcast.png"
image submod_blue_livingroom_oblique_snow = "mod_assets/location/Blue Livingroom(oblique)/blo_snow.png"

#Night images
image submod_blue_livingroom_oblique_night = "mod_assets/location/Blue Livingroom(oblique)/blo-n.png"
image submod_blue_livingroom_oblique_rain_night = "mod_assets/location/Blue Livingroom(oblique)/blo_rain-n.png"
image submod_blue_livingroom_oblique_overcast_night = "mod_assets/location/Blue Livingroom(oblique)/blo_overcast-n.png"
image submod_blue_livingroom_oblique_snow_night = "mod_assets/location/Blue Livingroom(oblique)/blo_snow-n.png"

#Sunset images
image submod_blue_livingroom_oblique_ss = "mod_assets/location/Blue Livingroom(oblique)/blo-ss.png"
image submod_blue_livingroom_oblique_rain_ss = "mod_assets/location/Blue Livingroom(oblique)/blo_rain-ss.png"
image submod_blue_livingroom_oblique_overcast_ss = "mod_assets/location/Blue Livingroom(oblique)/blo_overcast-ss.png"
image submod_blue_livingroom_oblique_snow_ss = "mod_assets/location/Blue Livingroom(oblique)/blo_snow-ss.png"


init -1 python:
    submod_blue_livingroom_oblique = MASFilterableBackground(
        # ID
        "submod_blue_livingroom_oblique",
        "蓝色客厅 - 斜视角",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_blue_livingroom_oblique_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_blue_livingroom_oblique_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_blue_livingroom_oblique_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_blue_livingroom_oblique_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_blue_livingroom_oblique_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_blue_livingroom_oblique_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_blue_livingroom_oblique_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_blue_livingroom_oblique_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_blue_livingroom_oblique_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_blue_livingroom_oblique_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_blue_livingroom_oblique_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_blue_livingroom_oblique_snow_ss",
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
        entry_pp=store.mas_background._blue_livingroom_oblique_entry,
        exit_pp=store.mas_background._blue_livingroom_oblique_exit,
        ex_props={"skip_outro": None}
    )


init -2 python in mas_background:
    def _blue_livingroom_oblique_entry(_old, **kwargs):
        """
        Entry programming point for blue_livingroom_oblique background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("blue_livingroom_oblique_switch_dlg"):
                store.pushEvent("blue_livingroom_oblique_switch_dlg")

        store.monika_chr.tablechair.table = "BL"
        store.monika_chr.tablechair.chair = "BL"

    def _blue_livingroom_oblique_exit(_new, **kwargs):
        """
        Exit programming point for blue_livingroom_oblique background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")

label blue_livingroom_oblique_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "这儿的空气还不错吧, [player]?",
            "蓝色的墙壁很漂亮吧!",
            "我喜欢这个房间...",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "还是喜欢原来的地方吗, [player]?",
            "充满回忆的地方...",
            "我们下回再去一趟吧.",
        ]))

    m 1hua "[switch_quip]"
    return

