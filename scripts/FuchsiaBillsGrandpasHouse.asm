FuchsiaBillsGrandpasHouse_Script:
	call EnableAutoTextBoxDrawing
	ret

FuchsiaBillsGrandpasHouse_TextPointers:
	def_text_pointers
	dw_const FuchsiaBillsGrandpasHouseMiddleAgedWomanText, TEXT_FUCHSIABILLSGRANDPASHOUSE_MIDDLE_AGED_WOMAN
	dw_const FuchsiaBillsGrandpasHouseBillsGrandpaText,    TEXT_FUCHSIABILLSGRANDPASHOUSE_BILLS_GRANDPA
	dw_const FuchsiaBillsGrandpasHouseYoungsterText,       TEXT_FUCHSIABILLSGRANDPASHOUSE_YOUNGSTER

FuchsiaBillsGrandpasHouseMiddleAgedWomanText:
	text "サファリ　ゾーンの　えんちょう"
	line "おとし　なのに　すごく　げんきよ"

	para "でも<⋯>「は」は"
	line "ぜんぶ　いれば　らしい　けど"
	done

FuchsiaBillsGrandpasHouseBillsGrandpaText:
	text_asm
	ld hl, RelocatedText_FuchsiaBillsGrandpasHouseBillsGrandpaText
	ld a, BANK(RelocatedText_FuchsiaBillsGrandpasHouseBillsGrandpaText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

FuchsiaBillsGrandpasHouseYoungsterText:
	text "マサキ　にいちゃん"
	line "じぶんで　あつめた　#も"
	cont "<PC>の　データに　してるよ！"

	para "みせて　もらった？"
	done
