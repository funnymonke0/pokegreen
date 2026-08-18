VermilionPidgeyHouse_Script:
	call EnableAutoTextBoxDrawing
	ret

VermilionPidgeyHouse_TextPointers:
	def_text_pointers
	dw_const VermilionPidgeyHouseYoungsterText, TEXT_VERMILIONPIDGEYHOUSE_YOUNGSTER
	dw_const VermilionPidgeyHousePidgeyText,    TEXT_VERMILIONPIDGEYHOUSE_PIDGEY
	dw_const VermilionPidgeyHouseLetterText,    TEXT_VERMILIONPIDGEYHOUSE_LETTER

VermilionPidgeyHouseYoungsterText:
	text "きたの　ヤマブキシティまで"
	line "ポッポに　てがみを"
	cont "とどけて　もらうのさ！"
	done

VermilionPidgeyHousePidgeyText:
	text "ポッポ『クルックー@"
	text_asm
	ld a, PIDGEY
	call PlayCry
	call WaitForSoundToFinish
	jp TextScriptEnd

VermilionPidgeyHouseLetterText:
	text_asm
	ld hl, RelocatedText_VermilionPidgeyHouseLetterText
	ld a, BANK(RelocatedText_VermilionPidgeyHouseLetterText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

