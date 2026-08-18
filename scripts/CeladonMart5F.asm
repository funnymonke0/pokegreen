CeladonMart5F_Script:
	jp EnableAutoTextBoxDrawing

CeladonMart5F_TextPointers:
	def_text_pointers
	dw_const CeladonMart5FGentlemanText,        TEXT_CELADONMART5F_GENTLEMAN
	dw_const CeladonMart5FSailorText,           TEXT_CELADONMART5F_SAILOR
	dw_const CeladonMart5FClerk1Text,           TEXT_CELADONMART5F_CLERK1
	dw_const CeladonMart5FClerk2Text,           TEXT_CELADONMART5F_CLERK2
	dw_const CeladonMart5FCurrentFloorSignText, TEXT_CELADONMART5F_CURRENT_FLOOR_SIGN

CeladonMart5FGentlemanText:
	text_asm
	ld hl, RelocatedText_CeladonMart5FGentlemanText
	ld a, BANK(RelocatedText_CeladonMart5FGentlemanText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeladonMart5FSailorText:
	text_asm
	ld hl, RelocatedText_CeladonMart5FSailorText
	ld a, BANK(RelocatedText_CeladonMart5FSailorText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeladonMart5FCurrentFloorSignText:
	text "５かい<⋯>ドラッグ　ストア"
	done
