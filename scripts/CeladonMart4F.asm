CeladonMart4F_Script:
	jp EnableAutoTextBoxDrawing

CeladonMart4F_TextPointers:
	def_text_pointers
	dw_const CeladonMart4FClerkText,            TEXT_CELADONMART4F_CLERK
	dw_const CeladonMart4FSuperNerdText,        TEXT_CELADONMART4F_SUPER_NERD
	dw_const CeladonMart4FYoungsterText,        TEXT_CELADONMART4F_YOUNGSTER
	dw_const CeladonMart4FCurrentFloorSignText, TEXT_CELADONMART4F_CURRENT_FLOOR_SIGN

CeladonMart4FSuperNerdText:
	text "かのじょに　プレゼントを　かうんだ"

	para "やっぱり　ピッピにんぎょう　だな！"
	line "にんき　あるんだよね！"
	done

CeladonMart4FYoungsterText:
	text_asm
	ld hl, RelocatedText_CeladonMart4FYoungsterText
	ld a, BANK(RelocatedText_CeladonMart4FYoungsterText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeladonMart4FCurrentFloorSignText:
	text_asm
	ld hl, RelocatedText_CeladonMart4FCurrentFloorSignText
	ld a, BANK(RelocatedText_CeladonMart4FCurrentFloorSignText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

