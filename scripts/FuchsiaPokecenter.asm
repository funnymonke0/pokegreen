FuchsiaPokecenter_Script:
	call Serial_TryEstablishingExternallyClockedConnection
	jp EnableAutoTextBoxDrawing

FuchsiaPokecenter_TextPointers:
	def_text_pointers
	dw_const FuchsiaPokecenterNurseText,            TEXT_FUCHSIAPOKECENTER_NURSE
	dw_const FuchsiaPokecenterRockerText,           TEXT_FUCHSIAPOKECENTER_ROCKER
	dw_const FuchsiaPokecenterCooltrainerFText,     TEXT_FUCHSIAPOKECENTER_COOLTRAINER_F
	dw_const FuchsiaPokecenterLinkReceptionistText, TEXT_FUCHSIAPOKECENTER_LINK_RECEPTIONIST

FuchsiaPokecenterNurseText:
	script_pokecenter_nurse

FuchsiaPokecenterRockerText:
	text_asm
	ld hl, RelocatedText_FuchsiaPokecenterRockerText
	ld a, BANK(RelocatedText_FuchsiaPokecenterRockerText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

FuchsiaPokecenterCooltrainerFText:
	text_asm
	ld hl, RelocatedText_FuchsiaPokecenterCooltrainerFText
	ld a, BANK(RelocatedText_FuchsiaPokecenterCooltrainerFText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

FuchsiaPokecenterLinkReceptionistText:
	script_cable_club_receptionist
