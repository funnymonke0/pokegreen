CinnabarPokecenter_Script:
	call Serial_TryEstablishingExternallyClockedConnection
	jp EnableAutoTextBoxDrawing

CinnabarPokecenter_TextPointers:
	def_text_pointers
	dw_const CinnabarPokecenterNurseText,            TEXT_CINNABARPOKECENTER_NURSE
	dw_const CinnabarPokecenterCooltrainerFText,     TEXT_CINNABARPOKECENTER_COOLTRAINER_F
	dw_const CinnabarPokecenterGentlemanText,        TEXT_CINNABARPOKECENTER_GENTLEMAN
	dw_const CinnabarPokecenterLinkReceptionistText, TEXT_CINNABARPOKECENTER_LINK_RECEPTIONIST

CinnabarPokecenterNurseText:
	script_pokecenter_nurse

CinnabarPokecenterCooltrainerFText:
	text_asm
	ld hl, RelocatedText_CinnabarPokecenterCooltrainerFText
	ld a, BANK(RelocatedText_CinnabarPokecenterCooltrainerFText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CinnabarPokecenterGentlemanText:
	text_asm
	ld hl, RelocatedText_CinnabarPokecenterGentlemanText
	ld a, BANK(RelocatedText_CinnabarPokecenterGentlemanText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CinnabarPokecenterLinkReceptionistText:
	script_cable_club_receptionist
