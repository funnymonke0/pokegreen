CeladonMart1F_Script:
	jp EnableAutoTextBoxDrawing

CeladonMart1F_TextPointers:
	def_text_pointers
	dw_const CeladonMart1FReceptionistText,     TEXT_CELADONMART1F_RECEPTIONIST
	dw_const CeladonMart1FDirectorySignText,    TEXT_CELADONMART1F_DIRECTORY_SIGN
	dw_const CeladonMart1FCurrentFloorSignText, TEXT_CELADONMART1F_CURRENT_FLOOR_SIGN

CeladonMart1FReceptionistText:
	text "いらっしゃいませ！"
	line "タマムシ　デパートに　ようこそ！"

	para "かく　フロアの　あんないは"
	line "みぎの　ボードを　ごらん　ください"
	done

CeladonMart1FDirectorySignText:
	text_asm
	ld hl, RelocatedText_CeladonMart1FDirectorySignText
	ld a, BANK(RelocatedText_CeladonMart1FDirectorySignText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeladonMart1FCurrentFloorSignText:
	text "１かい<⋯>サービス·カウンター"
	done
