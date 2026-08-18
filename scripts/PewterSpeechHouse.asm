PewterSpeechHouse_Script:
	jp EnableAutoTextBoxDrawing

PewterSpeechHouse_TextPointers:
	def_text_pointers
	dw_const PewterSpeechHouseGamblerText,   TEXT_PEWTERSPEECHHOUSE_GAMBLER
	dw_const PewterSpeechHouseYoungsterText, TEXT_PEWTERSPEECHHOUSE_YOUNGSTER

PewterSpeechHouseGamblerText:
	text "#を　そだてて　いくと"
	line "わざを　おぼえる！"

	para "しかし　ひとから　おそわらなければ"
	line "おぼえない　わざも　あるぞ"
	done

PewterSpeechHouseYoungsterText:
	text_asm
	ld hl, RelocatedText_PewterSpeechHouseYoungsterText
	ld a, BANK(RelocatedText_PewterSpeechHouseYoungsterText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

