Museum2F_Script:
	jp EnableAutoTextBoxDrawing

Museum2F_TextPointers:
	def_text_pointers
	dw_const Museum2FYoungsterText,        TEXT_MUSEUM2F_YOUNGSTER
	dw_const Museum2FGrampsText,           TEXT_MUSEUM2F_GRAMPS
	dw_const Museum2FScientistText,        TEXT_MUSEUM2F_SCIENTIST
	dw_const Museum2FBrunetteGirlText,     TEXT_MUSEUM2F_BRUNETTE_GIRL
	dw_const Museum2FHikerText,            TEXT_MUSEUM2F_HIKER
	dw_const Museum2FSpaceShuttleSignText, TEXT_MUSEUM2F_SPACE_SHUTTLE_SIGN
	dw_const Museum2FMoonStoneSignText,    TEXT_MUSEUM2F_MOON_STONE_SIGN

Museum2FYoungsterText:
	text "つきの　いしね<⋯>"

	para "そこらへんの　いしころと"
	line "どこが　ちがうんだろう？"
	done

Museum2FGrampsText:
	text_asm
	ld hl, RelocatedText_Museum2FGrampsText
	ld a, BANK(RelocatedText_Museum2FGrampsText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

Museum2FScientistText:
	text "こんげつは"
	line "うちゅう　はくらんかいを　やってます"
	done

Museum2FBrunetteGirlText:
	text "わたしね　わたしね"
	line "かわいいから　ピカチュウ　ほしい！"

	para "おとうさんに　とってきてね　って"
	line "おねがい　してるの"
	done

Museum2FHikerText:
	text "はい　はい！"
	line "ピカチュウだな！　こんどな！"
	done

Museum2FSpaceShuttleSignText:
	text "スペース　シャトル　コロンビアごう"
	done

Museum2FMoonStoneSignText:
	text "オツキミやまに　らっかした　ぶったい"
	line "たぶん<⋯>　つきの　いし"
	done
