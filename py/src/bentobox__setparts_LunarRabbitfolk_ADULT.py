import sims4.commands
import random
from sims.occult.occult_enums import OccultType
import services
from buffs.appearance_modifier.appearance_modifier import AppearanceModifier, AppearanceModifierPriority
from cas.cas import OutfitOverrideOptionFlags
from server_commands.argument_helpers import get_optional_target, OptionalTargetParam, OptionalSimInfoParam
from protocolbuffers import PersistenceBlobs_pb2
from sims4.resources import Types, get_resource_key


@sims4.commands.Command('bentobox.set_dreadnaut_stuff', command_type=sims4.commands.CommandType.Live)
def set_dreadnaut_stuff(opt_sim: OptionalTargetParam = None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    # Get Active Sim
    client = services.client_manager().get(_connection)
    sim = get_optional_target(opt_sim, _connection)
    sim_info = sim.sim_info
    sim_info_mermaid = sim_info.occult_tracker.get_occult_sim_info(OccultType.MERMAID)
    sim_info_human = sim_info.occult_tracker.get_occult_sim_info(OccultType.HUMAN)

    # UNFINISHED: Script was pasted in from old script that I didn't lose. I'll fix it later.
    # COURSE OF ACTION:
    # Get sim's color swatch stat values
    # Collect sim's part type traits
    # If part type trait x equals true/equipped, add it to the part collector and use a bullshit long ifelse tree to grab its swatch
    # ???
    # Profit?

    # Choose mimic type
    mimictypechoices = ['shrimp']

    mimictype = str(random.choice(mimictypechoices))

    output('mimic type chosen OK')

    if mimictype == 'shrimp':

        # Add shrimp trait for logging or whatever
        shrimp_naut_trait = 2459847263
        # Get the tuned trait instance from the tuning instance manager
        instance_manager = services.get_instance_manager(Types.TRAIT)
        trait_to_add = instance_manager.get(get_resource_key(shrimp_naut_trait, Types.TRAIT))

        sim_info.add_trait(trait_to_add)

        output('naut type trait added OK')

        mimiccolorchoices = ['natural', 'natural_rilli', 'natural_cherry']
        mimiccolor = str(random.choice(mimiccolorchoices))

        pearlcolor = [10979115762240474850, 10331098793114370613, 10331110887742280834, 10331953113649301267,
                      10331949815114416698, 10331947616091160208, 10332943773626130125, 10332947072161014818,
                      10332936077044732704, 10333935533114587314, 10333937732137843676, 10333931135068074382,
                      10333933334091330856, 10327170238067529582, 10327173536602414151, 10327162541486132037,
                      10328160898044358424, 10328158699021102078, 10328164196579243121, 10328153201462961023,
                      10329153757044443740, 10329152657532815489, 10329146060463046323, 10330112531184054479,
                      10330114730207310953, 10330115829718939172, 10330118028742195534]

        if mimiccolor == 'natural':
            output('color chosen OK')
            cas_mod_terror = []
            cas_mod_human = []

            randompearlcolor = int(random.choice(pearlcolor))
            cas_parts_terror = [12355679439800705167]
            cas_parts_human = [12871247961615640697, randompearlcolor]
            for cas_part in cas_parts_terror:
                terrorpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                           replace_with_random=False,
                                                           update_genetics=True, _is_combinable_with_same_type=True,
                                                           remove_conflicting=False, outfit_type_compatibility=None,
                                                           appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_terror.append(terrorpart)
                output('terrorpart appended OK')
            for cas_part in cas_parts_human:
                humanpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                          replace_with_random=False,
                                                          update_genetics=True, _is_combinable_with_same_type=True,
                                                          remove_conflicting=False, outfit_type_compatibility=None,
                                                          appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_human.append(humanpart)
                output('humanpart appended OK')

        if mimiccolor == 'natural_rilli':
            output('color chosen OK')
            cas_mod_terror = []
            cas_mod_human = []

            randompearlcolor = random.choice(pearlcolor)
            cas_parts_terror = [12353828961730804598]
            cas_parts_human = [17273572203857186166, randompearlcolor]
            for cas_part in cas_parts_terror:
                terrorpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                           replace_with_random=False,
                                                           update_genetics=True, _is_combinable_with_same_type=True,
                                                           remove_conflicting=False, outfit_type_compatibility=None,
                                                           appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_terror.append(terrorpart)
                output('terrorpart appended OK')
            for cas_part in cas_parts_human:
                humanpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                          replace_with_random=False,
                                                          update_genetics=True, _is_combinable_with_same_type=True,
                                                          remove_conflicting=False, outfit_type_compatibility=None,
                                                          appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_human.append(humanpart)
                output('humanpartappended OK')

        if mimiccolor == 'natural_cherry':
            output('color chosen OK')
            cas_mod_terror = []
            cas_mod_human = []

            randompearlcolor = random.choice(pearlcolor)
            cas_parts_terror = [12353834459288945655]
            cas_parts_human = [11014886159812428817, randompearlcolor]
            for cas_part in cas_parts_terror:
                terrorpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                           replace_with_random=False,
                                                           update_genetics=True, _is_combinable_with_same_type=True,
                                                           remove_conflicting=False, outfit_type_compatibility=None,
                                                           appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_terror.append(terrorpart)
                output('terrorpart appended OK')
            for cas_part in cas_parts_human:
                humanpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                          replace_with_random=False,
                                                          update_genetics=True, _is_combinable_with_same_type=True,
                                                          remove_conflicting=False, outfit_type_compatibility=None,
                                                          appearance_modifier_tag=None, expect_invalid_parts=False)
                cas_mod_human.append(humanpart)
                output('humanpart appended OK')

        # Permanently apply all modifiers
        sim_info.appearance_tracker.apply_permanent_appearance_modifiers(cas_mod_terror, 0,
                                                                         AppearanceModifierPriority.INVALID,
                                                                         True,
                                                                         OutfitOverrideOptionFlags.OVERRIDE_ALL_OUTFITS)
        output('applied mermaid parts OK')

        # Make the merform small
        appearance_attributes = PersistenceBlobs_pb2.BlobSimFacialCustomizationData()
        appearance_attributes.ParseFromString(sim_info.facial_attributes)

        sculpts = {16695722412344660175}  # sculpts ids go here
        appearance_attributes.sculpts.extend(sculpts)

        sim_info.facial_attributes = appearance_attributes.SerializeToString()
        sim_info.resend_facial_attributes()
        output('made merform small OK')

        # Add actually make a mermaid
        mermaid_trait = 199043
        # Get the tuned trait instance from the tuning instance manager
        instance_manager = services.get_instance_manager(Types.TRAIT)
        trait_to_add_two = instance_manager.get(get_resource_key(mermaid_trait, Types.TRAIT))

        sim_info.add_trait(trait_to_add_two)
        output('turned into mermaid OK')

        sim_info.appearance_tracker.apply_permanent_appearance_modifiers(cas_mod_terror, 0,
                                                                         AppearanceModifierPriority.INVALID,
                                                                         True,
                                                                         OutfitOverrideOptionFlags.OVERRIDE_ALL_OUTFITS)
        output('applied human parts OK')