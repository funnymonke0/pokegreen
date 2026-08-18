CeladonMansionRoofHouse_Script:
	jp EnableAutoTextBoxDrawing

CeladonMansionRoofHouse_TextPointers:
	def_text_pointers
	dw_const CeladonMansionRoofHouseHikerText,         TEXT_CELADONMANSION_ROOF_HOUSE_HIKER
	dw_const CeladonMansionRoofHouseEeveePokeballText, TEXT_CELADONMANSION_ROOF_HOUSE_EEVEE_POKEBALL

CeladonMansionRoofHouseHikerText:
	text_asm
	ld hl, RelocatedText_CeladonMansionRoofHouseHikerText
	ld a, BANK(RelocatedText_CeladonMansionRoofHouseHikerText)
	ldh [hLoadedROMBank], a
	ld [rROMB], a
	call PrintText
	ld a, [wCurMap]
	call SwitchToMapRomBank
	jp TextScriptEnd

CeladonMansionRoofHouseEeveePokeballText:
	text_asm
	lb bc, EEVEE, 25
	call GivePokemon
	jr nc, .party_full
	ld a, TOGGLE_CELADON_MANSION_EEVEE_GIFT
	ld [wToggleableObjectIndex], a
	predef HideObject
.party_full
	jp TextScriptEnd
