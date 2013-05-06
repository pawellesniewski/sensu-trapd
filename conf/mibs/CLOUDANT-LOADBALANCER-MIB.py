# PySNMP SMI module. Autogenerated from smidump -f python CLOUDANT-LOADBALANCER-MIB
# by libsmi2pysnmp-0.1.3 at Mon May  6 15:26:05 2013,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( cloudantTrapLevel, cloudantTrapMessage, ) = mibBuilder.importSymbols("CLOUDANT-PLATFORM-MIB", "cloudantTrapLevel", "cloudantTrapMessage")
( cloudantLoadBalancerMIB, cloudantModules, ) = mibBuilder.importSymbols("CLOUDANT-REG-MIB", "cloudantLoadBalancerMIB", "cloudantModules")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

cloudantLoadBalancerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 40277, 1, 1, 4)).setRevisions(("2012-07-30 03:00",))
if mibBuilder.loadTexts: cloudantLoadBalancerModule.setOrganization("Cloudant, Inc.")
if mibBuilder.loadTexts: cloudantLoadBalancerModule.setContactInfo("580 Harrison Ave., Boston, MA 02118, USA")
if mibBuilder.loadTexts: cloudantLoadBalancerModule.setDescription("Cloudant DB Core object and event definition MIB")
cloudantLoadBalancerObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 3, 2, 1))
if mibBuilder.loadTexts: cloudantLoadBalancerObjects.setDescription("Sub-tree for accessible objects in the MIB.")
cloudantLoadBalancerEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2))
if mibBuilder.loadTexts: cloudantLoadBalancerEvents.setDescription("A sub-tree for all the CLOUDANT-LOADBALANCER-MIB related events\nand traps.")

# Augmentions

# Notifications

cloudantLoadBalancerServerDown = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2, 1)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantLoadBalancerServerDown.setDescription("This event is generated when a backend server for the\nload balancer changes to status DOWN.")
cloudantLoadBalancerServerUp = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2, 2)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantLoadBalancerServerUp.setDescription("This event is generated when a backend server for the\nload balancer changes to status UP.")
cloudantLBConfigReloadFailEvent = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2, 3)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantLBConfigReloadFailEvent.setDescription("This event is generated when the load balancer fails to reload its\nconfiguration. cloudantTrapMessage will contain further details as\nto the cause of the error.")
cloudantLoadBalancerAllServersDown = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2, 4)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantLoadBalancerAllServersDown.setDescription("This critical event is generated when all backend servers for the\nspecified server change to status DOWN. As this is a critical \nsituation, it is recommended that this event be placed into a\nseparate class from cloudantLoadBalancerServerUp to prevent\nauto-clearing.")
cloudantLoadBalancerAllCustomerBackendsDown = NotificationType((1, 3, 6, 1, 4, 1, 40277, 3, 2, 2, 5)).setObjects(*(("CLOUDANT-PLATFORM-MIB", "cloudantTrapMessage"), ) )
if mibBuilder.loadTexts: cloudantLoadBalancerAllCustomerBackendsDown.setDescription("This critical event is generated when all backend servers for the\nspecified customer account change status to DOWN. As this is a \ncritical situation, it can only be cleared in the SNMP manager or\ntrap sink. It should never be auto-cleared.")

# Exports

# Module identity
mibBuilder.exportSymbols("CLOUDANT-LOADBALANCER-MIB", PYSNMP_MODULE_ID=cloudantLoadBalancerModule)

# Objects
mibBuilder.exportSymbols("CLOUDANT-LOADBALANCER-MIB", cloudantLoadBalancerModule=cloudantLoadBalancerModule, cloudantLoadBalancerObjects=cloudantLoadBalancerObjects, cloudantLoadBalancerEvents=cloudantLoadBalancerEvents)

# Notifications
mibBuilder.exportSymbols("CLOUDANT-LOADBALANCER-MIB", cloudantLoadBalancerServerDown=cloudantLoadBalancerServerDown, cloudantLoadBalancerServerUp=cloudantLoadBalancerServerUp, cloudantLBConfigReloadFailEvent=cloudantLBConfigReloadFailEvent, cloudantLoadBalancerAllServersDown=cloudantLoadBalancerAllServersDown, cloudantLoadBalancerAllCustomerBackendsDown=cloudantLoadBalancerAllCustomerBackendsDown)

