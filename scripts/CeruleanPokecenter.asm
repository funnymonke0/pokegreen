CeruleanPokecenter_Script:
	call Serial_TryEstablishingExternallyClockedConnection
	jp EnableAutoTextBoxDrawing

CeruleanPokecenter_TextPointers:
	def_text_pointers
	dw_const CeruleanPokecenterNurseText,            TEXT_CERULEANPOKECENTER_NURSE
	dw_const CeruleanPokecenterSuperNerdText,        TEXT_CERULEANPOKECENTER_SUPER_NERD
	dw_const CeruleanPokecenterGentlemanText,        TEXT_CERULEANPOKECENTER_GENTLEMAN
	dw_const CeruleanPokecenterLinkReceptionistText, TEXT_CERULEANPOKECENTER_LINK_RECEPTIONIST

CeruleanPokecenterLinkReceptionistText:
	script_cable_club_receptionist

CeruleanPokecenterNurseText:
	script_pokecenter_nurse

CeruleanPokecenterSuperNerdText:
	text_asm
	ld hl, RelocatedText_CeruleanPokecenterSuperNerdText
	ld a, BANK(RelocatedText_CeruleanPokecenterSuperNerdText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeruleanPokecenterGentlemanText:
	text_asm
	ld hl, RelocatedText_CeruleanPokecenterGentlemanText
	ld a, BANK(RelocatedText_CeruleanPokecenterGentlemanText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

