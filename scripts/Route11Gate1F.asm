Route11Gate1F_Script:
	jp EnableAutoTextBoxDrawing

Route11Gate1F_TextPointers:
	def_text_pointers
	dw_const Route11Gate1FGuardText, TEXT_ROUTE11GATE1F_GUARD

Route11Gate1FGuardText:
	text_asm
	ld hl, RelocatedText_Route11Gate1FGuardText
	ld a, BANK(RelocatedText_Route11Gate1FGuardText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

