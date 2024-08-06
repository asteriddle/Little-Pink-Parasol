import sims4.commands
import services
from buffs.appearance_modifier.appearance_modifier import AppearanceModifier, AppearanceModifierPriority
from cas.cas import OutfitOverrideOptionFlags
from server_commands.argument_helpers import get_optional_target, OptionalTargetParam, OptionalSimInfoParam
from protocolbuffers import PersistenceBlobs_pb2
from sims4.resources import Types, get_resource_key


@sims4.commands.Command('bentobox.setparts_deoxys', command_type=sims4.commands.CommandType.Live)
def setparts_deoxys(opt_sim: OptionalTargetParam = None, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    # Get Active Sim
    client = services.client_manager().get(_connection)
    sim = get_optional_target(opt_sim, _connection)
    sim_info = sim.sim_info


    # Add species trait
    deoxys_species_trait = 2459847263
    # Get the tuned trait instance from the tuning instance manager
    instance_manager = services.get_instance_manager(Types.TRAIT)
    trait_to_add = instance_manager.get(get_resource_key(deoxys_species_trait, Types.TRAIT))

    sim_info.add_trait(trait_to_add)

    output('deoxys species trait added OK')

        
    cas_mod_human = []

    cas_parts_human = [12871247961615640697]
    for cas_part in cas_parts_human:
        humanpart = AppearanceModifier.SetCASPart(cas_part=cas_part, should_toggle=False,
                                                          replace_with_random=False,
                                                          update_genetics=True, _is_combinable_with_same_type=True,
                                                          remove_conflicting=False, outfit_type_compatibility=None,
                                                          appearance_modifier_tag=None, expect_invalid_parts=False)
        cas_mod_human.append(humanpart)
        output('humanpart appended OK')

        
    # Make sim use deoxys body scuplt
    appearance_attributes = PersistenceBlobs_pb2.BlobSimFacialCustomizationData()
    appearance_attributes.ParseFromString(sim_info.facial_attributes)

    sculpts = {16695722412344660175}  # sculpts ids go here
    appearance_attributes.sculpts.extend(sculpts)

    sim_info.facial_attributes = appearance_attributes.SerializeToString()
    sim_info.resend_facial_attributes()
    output('made merform small OK')

    sim_info.appearance_tracker.apply_permanent_appearance_modifiers(cas_mod_human, 0,
                                                                         AppearanceModifierPriority.INVALID,
                                                                         True,
                                                                         OutfitOverrideOptionFlags.OVERRIDE_ALL_OUTFITS)
    output('applied human parts OK')