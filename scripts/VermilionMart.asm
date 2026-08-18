VermilionMart_Script:
	jp EnableAutoTextBoxDrawing

VermilionMart_TextPointers:
	def_text_pointers
	dw_const VermilionMartClerkText,        TEXT_VERMILIONMART_CLERK
	dw_const VermilionMartCooltrainerMText, TEXT_VERMILIONMART_COOLTRAINER_M
	dw_const VermilionMartCooltrainerFText, TEXT_VERMILIONMART_COOLTRAINER_F

VermilionMartCooltrainerMText:
	text_asm
	ld hl, RelocatedText_VermilionMartCooltrainerMText
	ld a, BANK(RelocatedText_VermilionMartCooltrainerMText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

VermilionMartCooltrainerFText:
	text "#は　つかう　ひとに　よって"
	line "よくも　わるくも　なる"
	cont "パートナーだと　おもうの"
	done
