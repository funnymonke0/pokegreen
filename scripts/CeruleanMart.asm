CeruleanMart_Script:
	jp EnableAutoTextBoxDrawing

CeruleanMart_TextPointers:
	def_text_pointers
	dw_const CeruleanMartClerkText,        TEXT_CERULEANMART_CLERK
	dw_const CeruleanMartCooltrainerMText, TEXT_CERULEANMART_COOLTRAINER_M
	dw_const CeruleanMartCooltrainerFText, TEXT_CERULEANMART_COOLTRAINER_F

CeruleanMartCooltrainerMText:
	text_asm
	ld hl, RelocatedText_CeruleanMartCooltrainerMText
	ld a, BANK(RelocatedText_CeruleanMartCooltrainerMText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeruleanMartCooltrainerFText:
	text "おみせでは　みた　こと　ないけど"
	line "ふしぎなアメ　しってる？"

	para "#が　いっきに　そだって"
	line "レベルが　あがる　らしいの"
	done
