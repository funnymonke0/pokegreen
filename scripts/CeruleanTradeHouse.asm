CeruleanTradeHouse_Script:
	jp EnableAutoTextBoxDrawing

CeruleanTradeHouse_TextPointers:
	def_text_pointers
	dw_const CeruleanTradeHouseGrannyText,  TEXT_CERULEANTRADEHOUSE_GRANNY
	dw_const CeruleanTradeHouseGamblerText, TEXT_CERULEANTRADEHOUSE_GAMBLER

CeruleanTradeHouseGrannyText:
	text_asm
	ld hl, RelocatedText_CeruleanTradeHouseGrannyText
	ld a, BANK(RelocatedText_CeruleanTradeHouseGrannyText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeruleanTradeHouseGamblerText:
	text_asm
	ld a, TRADE_FOR_LOLA
	ld [wWhichTrade], a
	predef DoInGameTradeDialogue
	jp TextScriptEnd
