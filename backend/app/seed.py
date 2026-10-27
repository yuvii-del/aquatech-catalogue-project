from sqlalchemy.orm import Session

from app.models import Brand, Category, Product


CLOUDINARY_BASE = (
    "https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/"
)


# Product details are copied from the supplied frontend PRODUCTS dataset.
# Review source claims against the official leaflet before publishing.
KENT_PRODUCTS = [{'name': 'KENT Sapphire IoT',
  'slug': 'kent-sapphire-iot',
  'model_number': 'KENT-SAPPHIRE-IOT',
  'mrp': 28000,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Sapphire_IoT.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Advanced Wi-Fi IoT remote mobile application pairing tracking.',
                 'Real-time structural digital purity display readout on front.',
                 'Active trace copper infusion with custom alkaline balance control.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Model Code', 'value': '111177B'},
                                {'name': 'Purification Technology',
                                 'value': 'RO + UF + UV + Alkaline + Active Copper + TDS Control + '
                                          'UV in Tank'},
                                {'name': 'Storage Capacity', 'value': '8 Litres'},
                                {'name': 'Purification Capacity', 'value': 'Up to 20 Litres/hour'},
                                {'name': 'Body Material', 'value': 'ABS Food-Grade Plastic'},
                                {'name': 'Mounting Type', 'value': 'Wall-mounting or Tabletop'},
                                {'name': 'Dimensions (L x W x H)',
                                 'value': '36 cm x 32 cm x 50 cm (360 x 320 x 500 mm)'},
                                {'name': 'Net Weight',
                                 'value': 'Approx. 8.30 kg to 10 kg (depending on specs sheet)'},
                                {'name': 'Power Consumption', 'value': '60 W'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 250V AC, 50Hz'},
                                {'name': 'Alkaline pH Range', 'value': '8.0 to 9.5'},
                                {'name': 'Max Feed TDS Level', 'value': 'Up to 1500 mg/L'},
                                {'name': 'Water Source Suitability',
                                 'value': 'Borewell, tanker, and municipal/tap water'}]}],
  'features': [{'title': 'IoT & Mobile App',
                'description': 'Real-time monitoring of water quality, filter and membrane life, '
                               'RO flow rate, and service history, with automatic service call '
                               'registration.'},
               {'title': 'Digital Display of Purity',
                'description': 'Live visual indicator displaying water quality and the purifier '
                               'operational status.'},
               {'title': 'UV LED in Tank',
                'description': 'Continuous ultraviolet disinfection inside the storage tank to '
                               'help prevent bacterial growth.'},
               {'title': 'Warranty & Service',
                'description': 'Includes a 1-year manufacturer warranty plus 3 years of free '
                               'extended service.'}]},
 {'name': 'KENT Sapphire',
  'slug': 'kent-sapphire',
  'model_number': 'KENT-SAPPHIRE',
  'mrp': 25000,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Sapphire.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Real-time digital purity monitor array displaying exact TDS.',
                 'Multi-stage mineral enrichment keeping vital salts intact.',
                 'Protective auto-flushing system extending core membrane lifecycle.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '8 Litres with level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + Copper + TDS '
                                          'Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, non-breakable plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment, Activated Carbon, RO Membrane, UF Filter, '
                                          'Post Carbon + Alkaline + Copper Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'},
                                {'name': 'Product Weight', 'value': 'Approximately 8.30 kg'},
                                {'name': 'Product Dimensions',
                                 'value': '360 mm (L) × 320 mm (W) × 500 mm (H)'}]}],
  'features': [{'title': 'Advanced IoT Control',
                'description': 'The IoT variant connects to a smartphone app via Wi-Fi to monitor '
                               'filter life, water purity levels, and errors, and supports '
                               'automatic service call registration.',
                'image': ''},
               {'title': 'Digital Display of Purity',
                'description': 'The built-in front display provides real-time information about '
                               'purified water quality (TDS), RO flow rate, and filter life.',
                'image': ''},
               {'title': 'Mineral RO™ Technology',
                'description': 'An integrated TDS control valve allows adjustment of the mineral '
                               'content retained in drinking water, including naturally occurring '
                               'minerals such as calcium and magnesium.',
                'image': ''},
               {'title': 'Alkaline & Copper Goodness',
                'description': 'The purifier combines alkaline and copper-related water treatment '
                               'features. The supplied product information states an alkaline pH '
                               'range of 8.0–9.5.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'A UV LED inside the 8-litre storage tank is designed to help '
                               'disinfect stored water and reduce bacterial regrowth.',
                'image': ''},
               {'title': 'Auto-Flush System',
                'description': 'The automatic flushing system rinses the RO membrane to help '
                               'remove scaling and debris and support membrane performance.',
                'image': ''},
               {'title': 'Fail-Safe Alarms',
                'description': 'Audible alerts notify users of conditions such as UV lamp failure '
                               'or the need to replace filter cartridges.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'The purifier automatically starts purification when the tank water '
                               'level drops and stops when the tank is full.',
                'image': ''}]},
 {'name': 'KENT Grand IoT',
  'slug': 'kent-grand-iot',
  'model_number': 'KENT-GRAND-IOT',
  'mrp': 28000,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Grand_IoT.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 '100% Zero Water Wastage recirculation system configuration.',
                 'Smart IoT application syncing for continuous oversight.',
                 'Spacious 9L reservoir combined with active copper technology.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '9 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + Copper + TDS '
                                          'Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, non-breakable transparent plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment filter, Activated Carbon block, RO Membrane, '
                                          'UF Filter, Post Carbon + Alkaline + Copper Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'},
                                {'name': 'Product Dimensions',
                                 'value': 'Approximately 400 mm (L) × 230 mm (W) × 540 mm (H)'}]}],
  'features': [{'title': 'Advanced IoT Intelligence',
                'description': 'Connects to a smartphone via Wi-Fi to monitor water quality '
                               'parameters, filter health, daily usage history, and maintenance '
                               'service requests.',
                'image': ''},
               {'title': 'Digital Display of Purity',
                'description': 'The front display provides real-time information about purified '
                               'water quality (TDS), filter life progression, and RO flow rate.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Uses a mineral retention control valve to adjust the minerals '
                               'retained in purified water.',
                'image': ''},
               {'title': 'Zero Water Wastage Technology',
                'description': 'The supplied product information describes a system that '
                               'recirculates rejected wastewater back into the overhead tank using '
                               'a booster pump.',
                'image': ''},
               {'title': 'Alkaline & Active Copper Enriched',
                'description': 'Combines alkaline treatment, with a stated pH range of 8.0–9.5, '
                               'and copper enrichment.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'An internal UV LED system inside the 9-litre storage tank is '
                               'designed to help disinfect stored water.',
                'image': ''},
               {'title': 'Completely Automated Operation',
                'description': 'Automatically starts refilling when the water level drops and '
                               'stops operation when the storage tank is full.',
                'image': ''},
               {'title': 'Fail-Safe Intelligent Alarms',
                'description': 'Audible alerts notify users of filter replacement requirements or '
                               'UV system failures.',
                'image': ''}]},
 {'name': 'KENT Grand Plus',
  'slug': 'kent-grand-plus',
  'model_number': 'KENT-GRAND-PLUS',
  'mrp': 25500,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Grand_Plus.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Industry-standard Zero Water Wastage eco-friendly configuration.',
                 'Advanced patented mechanical mineral TDS adjustment control knob.',
                 'High structural resilience with clean transparent visual chassis.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '9 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + Copper + TDS '
                                          'Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, transparent non-breakable plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment Filter, Activated Carbon Block, RO Membrane, '
                                          'UF Filter, Post Carbon + Alkaline + Copper Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'},
                                {'name': 'Product Dimensions',
                                 'value': 'Approximately 400 mm (L) × 230 mm (W) × 540 mm (H)'}]}],
  'features': [{'title': 'Zero Water Wastage Technology',
                'description': 'Uses a dedicated water recirculation system designed to return '
                               'rejected RO water to the overhead tank and reduce water wastage '
                               'during purification.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Features a TDS control valve that allows adjustment of the taste '
                               'and mineral content retained in purified water, including '
                               'naturally occurring minerals such as calcium and magnesium.',
                'image': ''},
               {'title': 'Alkaline & Active Copper',
                'description': 'Combines alkaline water treatment, with a stated pH range of '
                               '8.0–9.5, and copper enrichment.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'Uses an internal UV LED system inside the 9-litre storage tank to '
                               'help disinfect stored water and reduce bacterial growth.',
                'image': ''},
               {'title': 'Auto-Flush System',
                'description': 'Periodically flushes the RO membrane to help remove accumulated '
                               'salts and scaling, supporting filtration performance and membrane '
                               'maintenance.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'Automatically starts purification when the tank water level drops '
                               'and stops when the tank reaches full capacity.',
                'image': ''},
               {'title': 'Intelligent Fail-Safe Alarms',
                'description': 'Provides audible alerts for conditions such as UV system '
                               'malfunction or filter replacement requirements.',
                'image': ''}]},
 {'name': 'KENT Pearl IoT',
  'slug': 'kent-pearl-iot',
  'model_number': 'KENT-PEARL-IOT',
  'mrp': 29000,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Pearl_IoT.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Completely detachable modular 11-litre storage reservoir structure.',
                 'Full smartphone remote dashboard monitoring using IoT infrastructure.',
                 'Massive high-volume storage capacity perfect for family usage.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '11 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + Copper + TDS '
                                          'Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, transparent non-breakable plastic'},
                                {'name': 'Storage Tank Type',
                                 'value': 'Transparent and fully detachable for manual cleaning'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment Filter, Activated Carbon Block, RO Membrane, '
                                          'UF Filter, Post Carbon + Alkaline + Copper Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'}]}],
  'features': [{'title': 'Advanced IoT Control',
                'description': 'Connects to the KENT Service App through Wi-Fi to provide water '
                               'quality updates, filter-life tracking, remote troubleshooting, and '
                               'service complaint registration.',
                'image': ''},
               {'title': 'Digital Display Console',
                'description': 'Features a front-mounted digital display for viewing TDS levels, '
                               'RO flow rate, and remaining filter and membrane life.',
                'image': ''},
               {'title': 'Detachable 11L Storage Tank',
                'description': 'Features a removable transparent 11-litre storage tank designed to '
                               'make emptying and manual cleaning easier.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Uses an adjustable TDS controller to help regulate the mineral '
                               'content and taste of purified water.',
                'image': ''},
               {'title': 'Alkaline & Copper Infusion',
                'description': 'Combines alkaline treatment and copper enrichment. The supplied '
                               'product description states a target pH range of 8.0–9.5; confirm '
                               'this specification with the manufacturer.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'Uses an internal UV LED system intended to help control microbial '
                               'growth in stored water.',
                'image': ''},
               {'title': 'Zero Water Wastage Technology',
                'description': 'Uses a water recirculation system designed to return rejected RO '
                               'water to an overhead supply tank and reduce water wastage.',
                'image': ''},
               {'title': 'Smart Fail-Safe Alarms',
                'description': 'Provides audio alerts for conditions such as UV system failure and '
                               'filter cartridges that require replacement.',
                'image': ''}]},
 {'name': 'KENT Elegant',
  'slug': 'kent-elegant',
  'model_number': 'KENT-ELEGANT',
  'mrp': 23500,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Elegant.png',
  'highlights': ['Delivers a strong purification yield up to Up to 15 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Compact micro-footprint design explicitly built for tighter spaces.',
                 'Cost-efficient premium multi-filtration sequence infrastructure.',
                 'Reliable standalone automated pressure switches avoiding overflows.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 15 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '8 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UF + TDS Control + In-Tank UV'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, transparent non-breakable plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '250 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment Filter, Activated Carbon Block, RO Membrane, '
                                          'UF Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Compact Counter-top'},
                                {'name': 'Product Dimensions',
                                 'value': '340 mm (L) × 265 mm (W) × 505 mm (H)'}]}],
  'features': [{'title': 'Compact Wall-Mountable Design',
                'description': 'Features a space-saving design intended for smaller modular '
                               'kitchens, with wall-mounting or compact countertop installation '
                               'options.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Includes an adjustable TDS control valve to help regulate the '
                               'taste and mineral content of purified water, including naturally '
                               'occurring minerals such as calcium and magnesium.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'Features an internal UV LED system inside the 8-litre storage '
                               'tank, designed to help control microbial growth in stored water.',
                'image': ''},
               {'title': 'Multiple Purification Process',
                'description': 'Combines RO, UF, and TDS control with in-tank UV treatment to help '
                               'reduce various dissolved impurities and contaminants. Actual '
                               'removal performance depends on the source water and product '
                               'specifications.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'Automatically starts purification when the stored water level '
                               'drops and stops when the tank reaches its full level, helping '
                               'prevent overflow.',
                'image': ''},
               {'title': 'Source Versatility',
                'description': 'Designed for use with different water sources, including municipal '
                               'supplies, borewell water, and tanker supplies. Suitability depends '
                               'on the source water quality and the purifier’s operating limits.',
                'image': ''}]},
 {'name': 'KENT Crystal Plus',
  'slug': 'kent-crystal-plus',
  'model_number': 'KENT-CRYSTAL-PLUS',
  'mrp': 26500,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080260/KENT_Crystal_Plus.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'High-capacity 11L internal structural reservoir integration.',
                 'Dedicated 9.5 high-pH alkaline mineral conversion pathway.',
                 'Zero liquid discharge configuration via structural recirculation.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '11 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + TDS Control + '
                                          'In-Tank UV LED'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, transparent non-breakable plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment Filter, Activated Carbon Block, RO Membrane, '
                                          'UF Filter, Post Carbon + Alkaline Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'}]}],
  'features': [{'title': 'Zero Water Wastage Technology',
                'description': 'Uses an intelligent water recirculation system designed to return '
                               'rejected RO water to the overhead supply tank through a booster '
                               'pump, helping reduce water wastage.',
                'image': ''},
               {'title': 'Alkaline Water Enhancement',
                'description': 'Combines alkaline treatment with water purification. The supplied '
                               'product description states that the water pH can reach up to 9.5; '
                               'verify the exact range with the manufacturer.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Includes an adjustable TDS control valve to help regulate the '
                               'taste and mineral content of purified water, including naturally '
                               'occurring minerals such as calcium and magnesium.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'Features an internal UV LED system inside the 11-litre storage '
                               'tank, designed to help control microbial growth during water '
                               'storage.',
                'image': ''},
               {'title': 'High-Volume 11L Storage Tank',
                'description': 'Provides an 11-litre storage capacity with a water level '
                               'indicator, offering a larger water reserve than models with '
                               '8-litre or 9-litre tanks.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'Automatically starts purification when the stored water level '
                               'falls and stops when the tank reaches its full capacity.',
                'image': ''},
               {'title': 'Heavy Impurity Filtration',
                'description': 'The multi-stage purification system is designed to reduce various '
                               'impurities. Actual removal of contaminants such as arsenic, '
                               'fluoride, rust, pesticides, and microorganisms depends on the '
                               'product’s verified performance specifications and source water '
                               'quality.',
                'image': ''}]},
 {'name': 'KENT Crown Plus',
  'slug': 'kent-crown-plus',
  'model_number': 'KENT-CROWN-PLUS',
  'mrp': 26500,
  'category': 'domestic-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Crown_Plus.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Transparent Plastic.',
                 'Calibrated for easy Wall-mounted / Counter-top installation setups.',
                 'Premium aesthetic product styling available in multiple color tiers.',
                 'Expanded 11L backup tank architecture for off-grid safety.',
                 'Simultaneous active copper and adjusted alkaline mineral output.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '11 Litres with water level indicator'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + TDS Control + '
                                          'In-Tank UV LED'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, transparent non-breakable plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '100 Litres per day'},
                                {'name': 'Filter Cartridges',
                                 'value': 'Sediment Filter, Activated Carbon Block, RO Membrane, '
                                          'UF Filter, Post Carbon + Alkaline Filter'},
                                {'name': 'RO Membrane Type',
                                 'value': 'Thin Film Composite (TFC) RO Membrane'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Counter-top'}]}],
  'features': [{'title': 'Zero Water Wastage Technology',
                'description': 'Uses an intelligent water recirculation system designed to return '
                               'rejected RO water to the overhead supply tank through a booster '
                               'pump, helping reduce water wastage.',
                'image': ''},
               {'title': 'Alkaline Water Enhancement',
                'description': 'Combines alkaline treatment with water purification. The supplied '
                               'product description states that the water pH can reach up to 9.5; '
                               'verify the exact range with the manufacturer.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Includes an adjustable TDS control valve to help regulate the '
                               'taste and mineral content of purified water, including naturally '
                               'occurring minerals such as calcium and magnesium.',
                'image': ''},
               {'title': 'In-Tank UV LED Disinfection',
                'description': 'Features an internal UV LED system inside the 11-litre storage '
                               'tank, designed to help control microbial growth during water '
                               'storage.',
                'image': ''},
               {'title': 'High-Volume 11L Storage Tank',
                'description': 'Provides an 11-litre storage capacity with a water level '
                               'indicator, offering a larger water reserve than models with '
                               '8-litre or 9-litre tanks.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'Automatically starts purification when the stored water level '
                               'falls and stops when the tank reaches its full capacity.',
                'image': ''},
               {'title': 'Heavy Impurity Filtration',
                'description': 'The multi-stage purification system is designed to reduce various '
                               'impurities. Actual removal of contaminants such as arsenic, '
                               'fluoride, rust, pesticides, and microorganisms depends on the '
                               'product’s verified performance specifications and source water '
                               'quality.',
                'image': ''}]},
 {'name': 'KENT Sterling IoT',
  'slug': 'kent-sterling-iot',
  'model_number': 'KENT-STERLING-IOT',
  'mrp': 29000,
  'category': 'under-counter-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Sterling_IoT.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Under-the-counter / Under-sink installation setups.',
                 'Premium hidden under-sink architectural modular installation layout.',
                 'Full internet-connected telemetry for predictive system service.',
                 'High-pressure sealed hydrostatic tank framework giving constant flow.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '6 Litres hydrostatic tank'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + Alkaline + Copper + TDS '
                                          'Control'},
                                {'name': 'Body Material', 'value': 'ABS food-grade plastic'},
                                {'name': 'Installation Type',
                                 'value': 'Under-the-counter / Under-sink'},
                                {'name': 'Input Power Supply',
                                 'value': 'Single Phase 100–250V AC, 50–60 Hz'},
                                {'name': 'Power Consumption', 'value': '60 Watts'}]}],
  'features': [{'title': 'Under-the-Counter Smart Design',
                'description': 'Features a compact design intended for installation beneath '
                               'modular kitchen sinks, helping save countertop space.',
                'image': ''},
               {'title': 'Advanced IoT Intelligence',
                'description': 'Connects to a mobile application through Wi-Fi to monitor '
                               'available water-quality information, filter health, and service '
                               'requests.',
                'image': ''},
               {'title': 'Digital Display Console',
                'description': 'Provides a front-facing display for viewing supported '
                               'water-quality indicators, TDS information, and filter or membrane '
                               'life.',
                'image': ''},
               {'title': 'Alkaline & Active Copper Enrichment',
                'description': 'Combines alkaline treatment and copper enrichment as part of the '
                               'purification process. Verify the stated pH range and '
                               'health-related claims with the manufacturer.',
                'image': ''}]},
 {'name': 'KENT Excell Plus',
  'slug': 'kent-excell-plus',
  'model_number': 'KENT-EXCELL-PLUS',
  'mrp': 26500,
  'category': 'under-counter-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Excell_Plus.png',
  'highlights': ['Delivers a strong purification yield up to Up to 15 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Under-the-counter / Under-sink installation setups.',
                 'Concealed under-counter placement framework maximizing space.',
                 'Pressurized hydrostatic container delivering solid faucet velocity.',
                 'Computerized safety warning alerts for component replacements.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 15 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '7 Litres hydrostatic tank'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + TDS Control'},
                                {'name': 'Body Material', 'value': 'ABS food-grade plastic'},
                                {'name': 'Maximum Duty Cycle', 'value': '75 Litres per day'},
                                {'name': 'Installation Type',
                                 'value': 'Under-the-counter / Under-the-sink'},
                                {'name': 'Product Dimensions',
                                 'value': '390 mm (L) × 200 mm (W) × 520 mm (H)'}]}],
  'features': [{'title': 'Hydrostatic Storage Tank',
                'description': 'Uses a sealed storage reservoir designed to supply water through '
                               'the connected faucet. Confirm whether dispensing requires '
                               'electricity for the specific installation.',
                'image': ''},
               {'title': 'Mineral RO™ & TDS Control',
                'description': 'Includes a TDS control valve to help regulate the taste and '
                               'mineral content of purified water.',
                'image': ''},
               {'title': 'Fail-Safe Intelligent Alarms',
                'description': 'Provides alerts for maintenance conditions such as filter '
                               'replacement or UV system failure, where supported by the model.',
                'image': ''},
               {'title': 'Fully Automatic Operation',
                'description': 'Automatically starts purification when the tank requires refilling '
                               'and stops when the tank reaches its full level.',
                'image': ''}]},
 {'name': 'KENT Perk Star',
  'slug': 'kent-perk-star',
  'model_number': 'KENT-PERK-STAR',
  'mrp': 80000,
  'category': 'water-dispensers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Perk_Star.png',
  'highlights': ['Delivers a strong purification yield up to Up to 20 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Floor Standing Chiller / Dispenser installation setups.',
                 'Integrated chilling compressor unit outputting ice-cold streams.',
                 'Dual faucet temperature selectors for hot and chilled settings.',
                 'High durability vertical footprint optimized for heavy foot traffic.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 20 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '20 Litres total storage'},
                                {'name': 'Purification Technology',
                                 'value': 'Multi-stage RO + UV + UF + TDS Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade, non-breakable plastic'},
                                {'name': 'Dispensing Type',
                                 'value': 'Dual-temperature faucets (Hot and Cold)'},
                                {'name': 'Installation Type',
                                 'value': 'Floor-standing chiller / dispenser'},
                                {'name': 'Cooling Temperature',
                                 'value': '7°C–17°C, as specified in the supplied product '
                                          'description'}]}],
  'features': [{'title': 'Built-in Temperature Chilling',
                'description': 'Uses a compressor-based cooling system designed to provide chilled '
                               'water within the stated temperature range.',
                'image': ''},
               {'title': 'Inbuilt RO Purification',
                'description': 'Combines water dispensing functionality with an integrated RO '
                               'purification system and the listed supporting filtration '
                               'technologies.',
                'image': ''},
               {'title': 'Digital Display Status',
                'description': 'Includes front LED indicators intended to show operating status '
                               'for cooling, heating, and purification functions.',
                'image': ''},
               {'title': 'Corrosion-Resistant Storage',
                'description': 'Uses internal water reservoirs intended to resist corrosion and '
                               'help maintain water quality during storage.',
                'image': ''}]},
 {'name': 'KENT Perk',
  'slug': 'kent-perk',
  'model_number': 'KENT-PERK',
  'mrp': 66500,
  'category': 'water-dispensers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Perk.png',
  'highlights': ['Delivers a strong purification yield up to Up to 15 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Plastic.',
                 'Calibrated for easy Floor Standing Dispenser installation setups.',
                 'Direct plumbed bottleless configurations avoiding external water jars.',
                 'Integrated high-output dual thermostatic boiler and cooling setup.',
                 'Automated membrane micro-flush pathways reducing service overheads.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': 'Up to 15 Litres per hour (LPH)'},
                                {'name': 'Storage Tank Capacity',
                                 'value': '20 Litres internal storage reservoir'},
                                {'name': 'Purification Technology',
                                 'value': 'RO + UF + TDS Control'},
                                {'name': 'Maximum Duty Cycle', 'value': '120 Litres per day'},
                                {'name': 'Installation Type',
                                 'value': 'Floor-standing bottleless configuration'},
                                {'name': 'Cooling System',
                                 'value': 'Forced-convection, air-cooled condenser system'}]}],
  'features': [{'title': 'Bottleless Direct Line Connection',
                'description': 'Connects directly to a water supply line, eliminating the need for '
                               'external bottled-water jars.',
                'image': ''},
               {'title': 'Auto-Flushing Mechanism',
                'description': 'Periodically flushes the RO membrane to help reduce accumulated '
                               'scale and support routine purification performance.',
                'image': ''},
               {'title': 'Hot & Cold Water Dispensing',
                'description': 'Designed to provide hot water for beverages and chilled water for '
                               'refreshment through the same dispenser cabinet.',
                'image': ''},
               {'title': 'Double Protection Safety Cut-off',
                'description': 'Uses temperature-control and safety mechanisms intended to protect '
                               'against overheating and excessive cooling.',
                'image': ''}]},
 {'name': 'KENT Elite Star',
  'slug': 'kent-elite-star',
  'model_number': 'KENT-ELITE-STAR',
  'mrp': 60500,
  'category': 'commercial-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Elite_Star.png',
  'highlights': ['Delivers a strong purification yield up to Up to 50 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Commercial Chassis.',
                 'Calibrated for easy Wall-mounted Commercial installation setups.',
                 'Commercial high-flow 50 Litres Per Hour generation grid.',
                 'Dual-membrane parallel framework for non-stop production cycles.',
                 'Institutional telemetry screen console for quick operations logging.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': '50 Litres per hour (LPH), as supplied'},
                                {'name': 'Storage Tank Capacity',
                                 'value': 'Connects to external storage tanks / standard coolers'},
                                {'name': 'Purification Technology',
                                 'value': 'Commercial RO + UV + UF + TDS Control'},
                                {'name': 'Maximum Duty Cycle', 'value': '250 Litres per day'},
                                {'name': 'Power Consumption', 'value': '120 Watts'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted commercial chassis'},
                                {'name': 'Product Dimensions',
                                 'value': '410 mm (L) × 240 mm (W) × 480 mm (H)'}]}],
  'features': [{'title': 'High-Flow Production',
                'description': 'Specified with a 50 LPH purification rate for commercial '
                               'environments such as offices, schools, restaurants, and other '
                               'shared facilities.',
                'image': ''},
               {'title': 'Digital Display Console',
                'description': 'The supplied description identifies a front-mounted display for '
                               'viewing TDS information, filter-life status, and water flow '
                               'information.',
                'image': ''},
               {'title': 'Dual RO Membrane Support',
                'description': 'The supplied product description specifies two thin-film composite '
                               'RO membranes operating in parallel to support higher production '
                               'capacity.',
                'image': ''},
               {'title': 'TDS Level Adjustment',
                'description': 'Includes a mineral-retention and TDS-adjustment feature intended '
                               'to help regulate the taste of purified water.',
                'image': ''}]},
 {'name': 'KENT Elite 2 Plus',
  'slug': 'kent-elite-2-plus',
  'model_number': 'KENT-ELITE-2-PLUS',
  'mrp': 95000,
  'category': 'commercial-water-purifiers',
  'image_url': 'https://res.cloudinary.com/gxybnegl/image/upload/v1793080262/KENT_Elite_2_Plus.png',
  'highlights': ['Delivers a strong purification yield up to Up to 100 LPH.',
                 'Features a durable housing engineered with ABS Food-Grade Commercial Chassis.',
                 'Calibrated for easy Wall-mounted Commercial installation setups.',
                 'Massive high-volume 100 LPH multi-stage filtration grid.',
                 'Advanced double-stage industrial pollutant separation path.',
                 'Ideal large institutional architecture tracking pressure metrics.'],
  'specifications': [{'title': 'Key Specifications',
                      'items': [{'name': 'Purification Production Rate',
                                 'value': '100 Litres per hour (LPH), as supplied'},
                                {'name': 'Storage Tank Capacity',
                                 'value': 'Designed for external tanks / institutional coolers'},
                                {'name': 'Purification Technology',
                                 'value': 'Double-stage commercial RO + UV + UF + TDS Control'},
                                {'name': 'Body Material',
                                 'value': 'ABS food-grade plastic mounting structure'},
                                {'name': 'Filter Configuration',
                                 'value': 'Triple sediment filters and high-capacity carbon blocks '
                                          'with extra-large RO housings'},
                                {'name': 'Installation Type',
                                 'value': 'Wall-mounted / Multi-cooler configuration'}]}],
  'features': [{'title': 'Double-Stage Commercial Purification',
                'description': 'Uses a two-stage RO purification configuration, as described in '
                               'the supplied specifications, for commercial water treatment '
                               'applications.',
                'image': ''},
               {'title': 'High-Capacity 100 LPH Production',
                'description': 'Specified for high-volume water demand in larger facilities and '
                               'public venues. Confirm the rated production capacity and operating '
                               'conditions with the manufacturer.',
                'image': ''},
               {'title': 'Mineral RO™ Core',
                'description': 'Includes a stated mineral-retention feature intended to help '
                               'regulate the mineral content and taste of purified water.',
                'image': ''},
               {'title': 'Standalone Automation',
                'description': 'Uses automatic pressure or tank-level controls, as specified, to '
                               'manage purification start-up and shut-off with less manual '
                               'intervention.',
                'image': ''}]}]


CATEGORY_DATA = [
    {"name": "Domestic Water Purifiers", "slug": "domestic-water-purifiers"},
    {"name": "Under-Counter Water Purifiers", "slug": "under-counter-water-purifiers"},
    {"name": "Water Dispensers", "slug": "water-dispensers"},
    {"name": "Commercial Water Purifiers", "slug": "commercial-water-purifiers"},
]


def seed_database(db: Session) -> None:
    try:
        brand = db.query(Brand).filter(Brand.slug == "kent").first()
        if brand is None:
            brand = Brand(
                name="KENT",
                slug="kent",
                description="KENT water purification products",
            )
            db.add(brand)
            db.flush()

        categories = {}
        for item in CATEGORY_DATA:
            category = db.query(Category).filter(Category.slug == item["slug"]).first()
            if category is None:
                category = Category(**item)
                db.add(category)
                db.flush()
            categories[item["slug"]] = category

        for item in KENT_PRODUCTS:
            product = db.query(Product).filter(Product.slug == item["slug"]).first()

            product_values = {
                "name": item["name"],
                "slug": item["slug"],
                "model_number": item["model_number"],
                "description": f"{item['name']} water purifier.",
                "mrp": item["mrp"],
                "image_url": item["image_url"],
                "featured": False,
                "brand_id": brand.id,
                "category_id": categories[item["category"]].id,
                "highlights": item["highlights"],
                "specifications": item["specifications"],
                "features": item["features"],
            }

            if product is None:
                product = Product(**product_values)
                db.add(product)
            else:
                for key, value in product_values.items():
                    setattr(product, key, value)

        db.commit()
        print("KENT catalogue seed completed successfully.")

    except Exception:
        db.rollback()
        raise
