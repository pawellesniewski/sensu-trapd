# PySNMP SMI module. Autogenerated from smidump -f python CLOUDANT-PLATFORM-MIB
# by libsmi2pysnmp-0.1.3 at Mon Feb 18 16:14:50 2013,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( cloudantModules, cloudantPlatformMIB, ) = mibBuilder.importSymbols("CLOUDANT-REG-MIB", "cloudantModules", "cloudantPlatformMIB")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class CloudantReal(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class EventSeverity(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(5,0,1,4,6,2,3,7,)
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), )
    

# Objects

cloudantPlatformModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 40277, 1, 1, 2)).setRevisions(("2012-07-30 02:35",))
if mibBuilder.loadTexts: cloudantPlatformModule.setOrganization("Cloudant, Inc.")
if mibBuilder.loadTexts: cloudantPlatformModule.setContactInfo("580 Harrison Ave., Boston, MA 02118, USA")
if mibBuilder.loadTexts: cloudantPlatformModule.setDescription("Cloudant Platform Global definitions and textual conventions MIB")
cloudantPlatformObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 2, 1, 1))
if mibBuilder.loadTexts: cloudantPlatformObjects.setDescription("Sub-tree for accessible objects in the MIB.")
cloudantTrapLevel = MibScalar((1, 3, 6, 1, 4, 1, 40277, 2, 1, 1, 1), EventSeverity().clone('alert')).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: cloudantTrapLevel.setDescription("The error level of the particular notification.")
cloudantTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 40277, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10240))).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: cloudantTrapMessage.setDescription("The string being passed up from the object itself.\n\nThis string should include sufficient information to\nunderstand the message.\n\nThe object has often preprocessed various parameters\ninto the string provided with the trap.")
cloudantPlatformEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 2, 1, 2))
if mibBuilder.loadTexts: cloudantPlatformEvents.setDescription("A sub-tree for all the CLOUDANT-PLATFORM-MIB related events\nand traps.")

# Augmentions

# Notifications

cloudantGenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 40277, 2, 1, 2, 1)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel"), ("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantGenericTrap.setDescription("A cloudantGenericTrap is sent when an event occurs for which a\nspecific trap hasn't been identified.\n\nThe intention is that this will generally represent an event that \ndoes not normally generate a trap but which got promoted to a trap\ndue to severity level.\n\nIt is also the case that this may occasionally represent an event\nfor which we were temporarily unable to define a specific trap due\nto time constraints.\n\nThe cloudantTrapMessage parameter will usually contain a fairly full\ndescription of what event is being reported.")
cloudantGenericTrapNoArgs = NotificationType((1, 3, 6, 1, 4, 1, 40277, 2, 1, 2, 31337)).setObjects(*() )
if mibBuilder.loadTexts: cloudantGenericTrapNoArgs.setDescription("A cloudantGenericTrapNoArgs is sent when an almost totally unknown\nevent occurs. It should not be seen outside of internal testing.")

# Exports

# Module identity
mibBuilder.exportSymbols("CLOUDANT-PLATFORM-MIB", PYSNMP_MODULE_ID=cloudantPlatformModule)

# Types
mibBuilder.exportSymbols("CLOUDANT-PLATFORM-MIB", CloudantReal=CloudantReal, EventSeverity=EventSeverity)

# Objects
mibBuilder.exportSymbols("CLOUDANT-PLATFORM-MIB", cloudantPlatformModule=cloudantPlatformModule, cloudantPlatformObjects=cloudantPlatformObjects, cloudantTrapLevel=cloudantTrapLevel, cloudantTrapMessage=cloudantTrapMessage, cloudantPlatformEvents=cloudantPlatformEvents)

# Notifications
mibBuilder.exportSymbols("CLOUDANT-PLATFORM-MIB", cloudantGenericTrap=cloudantGenericTrap, cloudantGenericTrapNoArgs=cloudantGenericTrapNoArgs)

