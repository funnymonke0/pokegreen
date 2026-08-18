SSAnne1F_Script:
	call EnableAutoTextBoxDrawing
	ret

SSAnne1F_TextPointers:
	def_text_pointers
	dw_const SSAnne1FWaiterText, TEXT_SSANNE1F_WAITER
	dw_const SSAnne1FSailorText, TEXT_SSANNE1F_SAILOR

SSAnne1FWaiterText:
	text_asm
	ld hl, RelocatedText_SSAnne1FWaiterText
	ld a, BANK(RelocatedText_SSAnne1FWaiterText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

SSAnne1FSailorText:
	text "この　ふねの　おきゃくは"
	line "ながたびに　たいくつ　してる！"

	para "ひま　つぶしに　たたかいを"
	line "いどんで　くる　ひとも　いるかも"
	done
