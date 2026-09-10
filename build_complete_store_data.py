import json
import hashlib

images_map = {
    "Laptop": [
        "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop RAM": [
        "https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop SSD": [
        "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Display": [
        "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1585060544812-6b45742d762f?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Battery": [
        "https://images.unsplash.com/photo-1588508065123-287b28e013da?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1619725002198-6a689b72f41d?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Keyboard": [
        "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Cooler": [
        "https://images.unsplash.com/photo-1587202372634-32705e3bf49c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1588508065123-287b28e013da?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Charger": [
        "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1622445262464-84b1456045b6?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Motherboard": [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Wireless": [
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Thermal": [
        "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1586105251261-72a756497a11?auto=format&fit=crop&w=800&q=80"
    ],
    "Laptop Chassis": [
        "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1586953208448-b95a79798f07?auto=format&fit=crop&w=800&q=80"
    ],
    "Buds": [
        "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=800&q=80"
    ],
    "Headsets": [
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1545127398-14699f92334b?auto=format&fit=crop&w=800&q=80"
    ],
    "Chargers": [
        "https://images.unsplash.com/photo-1622445262464-84b1456045b6?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1609592424360-1596e1b6cb41?auto=format&fit=crop&w=800&q=80"
    ],
    "Smartwatches": [
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1510017803434-a899398421b3?auto=format&fit=crop&w=800&q=80"
    ],
    "Apple_Phone": [
        "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1530319067432-f2a729c03db5?auto=format&fit=crop&w=600&q=80"
    ],
    "Samsung_Phone": [
        "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1584006682522-dc17d6c0d963?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=600&q=80"
    ],
    "Android_Phone": [
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&w=600&q=80",
        "https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=600&q=80"
    ]
}

all_products = []
prod_id = 1

def add_product(name, brand, category, subcategory, price, tag, desc, features, specs, inTheBox, img_key="Laptop", warranty="1 Year Official Warranty", compatibleModel="", ramStorage=""):
    global prod_id
    pool = images_map.get(img_key, images_map["Android_Phone"])
    idx = int(hashlib.md5(f"{name}_{prod_id}".encode('utf-8')).hexdigest(), 16) % len(pool)
    img = pool[idx]
    gallery = pool.copy()
    if img in gallery:
        gallery.remove(img)
    gallery.insert(0, img)
    
    old_price = round(price * 1.25, 2)
    discount = "20% OFF"
    if price < 2000:
        old_price = round(price * 1.35, 2)
        discount = "25% OFF"
    elif price > 50000:
        old_price = round(price * 1.20, 2)
        discount = "15% OFF"

    p = {
        "id": prod_id,
        "name": name,
        "brand": brand,
        "category": category,
        "subcategory": subcategory,
        "compatibleModel": compatibleModel if compatibleModel else f"{brand} Compatible Series",
        "series": f"{brand} {category}",
        "ramStorage": ramStorage if ramStorage else (specs.get("Memory") or "Standard Spec"),
        "price": price,
        "oldPrice": old_price,
        "discount": discount,
        "tag": tag,
        "rating": round(4.6 + (prod_id % 4) * 0.1, 1),
        "ratingCount": 120 + (prod_id * 17) % 650,
        "image": img,
        "images": gallery,
        "desc": desc,
        "features": features,
        "specs": specs,
        "usage": "Direct plug & play or professional installation recommended with anti-static safety precautions.",
        "inTheBox": inTheBox,
        "warranty": warranty
    }
    all_products.append(p)
    prod_id += 1
    return p

# =========================================================================
# 1. ALL 166 SMARTPHONES (25+ GLOBAL BRANDS)
# =========================================================================

smartphone_brands = {
    "Apple": ["iPhone 16 Pro Max", "iPhone 16 Pro", "iPhone 16 Plus", "iPhone 16", "iPhone 15 Pro Max", "iPhone 15 Pro", "iPhone 15", "iPhone 14 Pro", "iPhone 14 Plus", "iPhone 14", "iPhone 13 Pro", "iPhone 13 Mini", "iPhone 13", "iPhone 12", "iPhone SE 3rd Gen"],
    "Samsung": ["Galaxy S26 Ultra", "Galaxy S26+", "Galaxy S26", "Galaxy S25 Edge", "Galaxy S24 Ultra", "Galaxy S24 FE", "Galaxy Z Fold 8", "Galaxy Z Flip 8", "Galaxy A57 5G", "Galaxy A55 5G", "Galaxy A36 5G", "Galaxy A27 5G", "Galaxy M47 5G", "Galaxy F70 Pro"],
    "Vivo": ["Vivo X100 Ultra", "Vivo X100 Pro", "Vivo X90 Pro", "Vivo V40 Pro 5G", "Vivo V40e", "Vivo V30 Pro", "Vivo T3 Pro 5G", "Vivo T3x 5G", "Vivo Y200 5G", "Vivo Y28 5G"],
    "OnePlus": ["OnePlus 15 5G", "OnePlus 13 5G", "OnePlus 12 5G", "OnePlus 15R 5G", "OnePlus 13R 5G", "OnePlus 12R 5G", "OnePlus Open Foldable", "OnePlus Nord 6 5G", "OnePlus Nord 4 5G", "OnePlus Nord CE 4 5G", "OnePlus Nord CE 6 Lite 5G"],
    "Xiaomi": ["Xiaomi 15 Pro", "Xiaomi 14 Ultra", "Xiaomi 14 Pro", "Redmi Note 14 Pro+ 5G", "Redmi Note 14 Pro 5G", "Redmi Note 13 Pro 5G", "Redmi K80 Pro", "Redmi Turbo 4", "Redmi 14C", "Redmi 13C 5G", "Redmi A4 5G"],
    "Realme": ["Realme GT 7 Pro", "Realme GT 6 5G", "Realme 14 Pro+ 5G", "Realme 13 Pro+ 5G", "Realme 13 5G", "Realme P2 Pro 5G", "Realme Narzo 70 Pro 5G", "Realme C67 5G", "Realme C65"],
    "Oppo": ["Oppo Find X8 Pro", "Oppo Find N3 Flip", "Oppo Reno 13 Pro 5G", "Oppo Reno 12 Pro", "Oppo F27 Pro+ 5G", "Oppo F25 Pro 5G", "Oppo K12x 5G", "Oppo A3 Pro 5G"],
    "POCO": ["POCO F6 Pro 5G", "POCO F6 5G", "POCO F5 5G", "POCO X6 Pro 5G", "POCO X6 Neo 5G", "POCO M6 Pro 5G", "POCO M6 Plus 5G", "POCO C65"],
    "Google": ["Google Pixel 9 Pro XL", "Google Pixel 9 Pro", "Google Pixel 9", "Google Pixel 8a", "Google Pixel 8 Pro", "Google Pixel 8", "Google Pixel 7a", "Google Pixel Fold"],
    "Motorola": ["Moto Edge 50 Ultra", "Moto Edge 50 Pro 5G", "Moto Edge 50 Fusion", "Moto Razr 50 Ultra", "Moto G85 5G", "Moto G64 5G", "Moto G34 5G", "Moto Edge 40 Neo"],
    "Infinix": ["Infinix GT 30 Pro", "Infinix GT 20 Pro", "Infinix ZERO Flip 5G", "Infinix ZERO 40 5G", "Infinix Note 50 Pro+ 5G", "Infinix Note 40 Pro 5G", "Infinix Hot 50 5G", "Infinix Smart 9"],
    "Tecno": ["Tecno Phantom V Fold 2", "Tecno Phantom X2 Pro", "Tecno Camon 30 Premier 5G", "Tecno Pova 6 Pro 5G", "Tecno Spark 20 Pro+"],
    "Honor": ["Honor Magic 6 Pro", "Honor Magic V2 Fold", "Honor 200 Pro 5G", "Honor 90 5G", "Honor X9b 5G"],
    "LG": ["LG Velvet 5G Dual Screen", "LG Wing Rotating 5G", "LG V60 ThinQ 5G", "LG G8X ThinQ Dual", "LG K92 5G"],
    "Huawei": ["Huawei Pura 70 Ultra", "Huawei Mate 60 Pro", "Huawei Mate X5 Foldable", "Huawei Nova 12 Pro", "Huawei P60 Pro"],
    "Asus": ["Asus ROG Phone 8 Pro 5G", "Asus ROG Phone 7 Ultimate", "Asus Zenfone 11 Ultra", "Asus Zenfone 10"],
    "Lenovo": ["Lenovo Legion Y90 Gaming", "Lenovo Legion Phone Duel 2", "Lenovo K14 Plus"],
    "Lava": ["Lava Agni 3 5G Dual AMOLED", "Lava Agni 2 5G", "Lava Blaze Curve 5G", "Lava Blaze Duo 5G", "Lava Yuva 3 Pro", "Lava Storm 5G"],
    "itel": ["itel S25 Ultra", "itel P55 5G", "itel Color Pro 5G", "itel A100 Pro", "itel Super Guru 4G Max"],
    "I KALL": ["I KALL Z19 Pro Ultra", "I KALL Z13 4G", "I KALL S2 Pro", "I KALL I7 Pro 4G", "I KALL K42 Flip", "I KALL K99 Pro Rugged"],
    "TCL": ["TCL 50 XL 5G", "TCL 40 NXTPAPER", "TCL 30 SE"],
    "Karbonn": ["Karbonn Platinum P9", "Karbonn Titanium S9 Plus", "Karbonn K9 Smart 4G"],
    "Acer": ["Acer Sospiro A60", "Acer Liquid Z6 Plus"],
    "Microsoft": ["Microsoft Surface Duo 2 5G", "Microsoft Surface Duo Dual-Screen"],
    "Croma": ["Croma Wave 5G Phone", "Croma Stellar Pro"]
}

for brand, models in smartphone_brands.items():
    img_key = "Apple_Phone" if brand == "Apple" else ("Samsung_Phone" if brand == "Samsung" else "Android_Phone")
    for m in models:
        m_lower = m.lower()
        price = 24999.0
        tag = "5G Smartphone"
        ram_storage = "8GB RAM + 128GB • 5G"
        
        if "ultra" in m_lower or "pro max" in m_lower or "fold" in m_lower or "flip" in m_lower or "pura" in m_lower or "rog" in m_lower or "duo" in m_lower:
            price = 79999.0
            tag = "Flagship Ultra"
            ram_storage = "16GB RAM + 512GB • 5G"
        elif "pro" in m_lower or "plus" in m_lower or "edge" in m_lower or "gt" in m_lower or "magic" in m_lower:
            price = 42999.0
            tag = "Pro Performance"
            ram_storage = "12GB RAM + 256GB • 5G"
        elif "lite" in m_lower or "c65" in m_lower or "smart" in m_lower or "a4" in m_lower or "y28" in m_lower:
            price = 8999.0
            tag = "Budget 5G"
            ram_storage = "6GB RAM + 128GB • 5G"
        elif "i kall" in m_lower or "karbonn" in m_lower or "itel" in m_lower or "croma" in m_lower:
            price = 5999.0
            tag = "Value Essential"
            ram_storage = "4GB RAM + 64GB"

        add_product(
            name=m,
            brand=brand,
            category="Smartphones",
            subcategory="5G Smartphones",
            price=price,
            tag=tag,
            desc=f"Official 100% genuine brand-sealed {m} smartphone featuring high-refresh AMOLED screen, multi-lens camera system, all-day battery, and multi-band 5G VoLTE support with 1 Year Official Brand IMEI Warranty.",
            features=[
                "100% Genuine Factory Sealed Pack with 1-Year Official Brand Warranty",
                "Ultra-Fast Multi-Band 5G & VoLTE Dual SIM Support",
                "High Refresh Rate AMOLED / HD+ Vivid Display with Gorilla Glass Protection",
                "High Density Battery with Fast Power Delivery Adapter Included"
            ],
            specs={
                "Network": "5G VoLTE (Dual SIM)",
                "Brand": brand,
                "Model": m,
                "Memory": ram_storage,
                "Condition": "Brand New Factory Sealed Box",
                "Warranty": "1 Year Official Manufacturer Warranty"
            },
            inTheBox=f"1x {m} Smartphone, 1x Fast Power Adapter, 1x Type-C Cable, 1x SIM Ejector, 1x Protective Case, 1x User Manual",
            img_key=img_key,
            warranty="1 Year Official Brand Warranty",
            compatibleModel=m,
            ramStorage=ram_storage
        )

print(f"Generated {len([p for p in all_products if p['category']=='Smartphones'])} Smartphones!")

# =========================================================================
# 2. 160+ HIGH-PERFORMANCE LAPTOP COMPONENTS ACROSS TOP BRANDS
# =========================================================================

# A. RAM COMPONENTS (25 Items)
ram_configs = [
    ("16GB DDR5 5600MHz CL46 SO-DIMM Laptop High-Speed Memory Module", 4299, "DDR5 5600MHz", "Ultra-fast DDR5 SODIMM laptop memory upgrade with built-in on-die ECC for extreme multitasking and low power draw."),
    ("32GB (2x16GB) DDR5 5600MHz Dual-Channel Laptop RAM Upgrade Kit", 7999, "Dual-Channel 32GB", "High-performance dual channel 32GB DDR5 5600MHz SO-DIMM kit optimized for gaming laptops and CAD workstations."),
    ("64GB (2x32GB) DDR5 5600MHz Extreme High-Density Laptop Memory Kit", 15499, "Pro 64GB DDR5", "Industrial-grade 64GB DDR5 high density SODIMM memory kit engineered for video editors, AI model developers and engineers."),
    ("16GB DDR4 3200MHz CL22 1.2V SO-DIMM Low Voltage Laptop RAM", 2499, "DDR4 3200MHz", "Reliable 16GB DDR4 SO-DIMM upgrade operating at 3200MHz at 1.2V for legacy Intel 10th/11th/12th Gen & AMD Ryzen laptops."),
    ("32GB (2x16GB) DDR4 3200MHz Dual-Channel Gaming SO-DIMM Kit", 4899, "DDR4 Gaming Kit", "Matched dual-channel DDR4 memory kit designed for zero latency and smooth framerates in gaming and creative workflows.")
]

for b in ["Dell", "HP", "Lenovo", "ASUS", "Acer"]:
    for title, price, tag, desc in ram_configs:
        name = f"{b} {title}"
        add_product(
            name=name,
            brand=b,
            category="Laptop Components",
            subcategory="Laptop RAM",
            price=price,
            tag=tag,
            desc=f"{desc} Certified 100% compatible with {b} gaming, business, and ultrabook laptops.",
            features=[
                "High Speed Multi-Thread Performance with 1.1V / 1.2V Energy Efficiency",
                "On-Die ECC Error Correction for Rock-Solid System Stability",
                "Tested for 100% Plug-and-Play Compatibility with Intel & AMD Platforms",
                "Gold-Plated 262-Pin SO-DIMM Contacts for Maximum Signal Integrity"
            ],
            specs={"Memory Type": "DDR5 / DDR4 SO-DIMM", "Speed": "Up to 5600 MHz", "Voltage": "1.1V", "Form Factor": "SO-DIMM 262-Pin", "Warranty": "5 Years Limited Brand Warranty"},
            inTheBox="1x Laptop RAM Module, 1x Anti-Static Shield Box, 1x Installation Quick Guide",
            img_key="Laptop RAM",
            warranty="5 Years Replacement Warranty",
            compatibleModel=f"{b} Latitude / Omen / Legion / ROG / Predator Series"
        )

# B. NVMe PCIe SSD STORAGE COMPONENTS (20 Items)
ssd_configs = [
    ("1TB Gen4 x4 NVMe M.2 2280 High-Speed Solid State Drive (7450 MB/s)", 6999, "7450 MB/s Gen4", "Blazing fast PCIe 4.0 NVMe M.2 SSD with dynamic thermal guard, sequential read speeds up to 7450MB/s and low-power controller."),
    ("2TB Gen4 x4 NVMe M.2 2280 Extreme Performance SSD with Graphene Thermal Shield", 12999, "2TB Gen4 Pro", "High endurance 2TB M.2 PCIe Gen4 x4 internal SSD featuring 1200 TBW endurance and graphene heat dissipating sticker."),
    ("4TB Gen4 x4 NVMe M.2 2280 Ultra-Capacity High Endurance SSD", 24999, "4TB Huge Storage", "Massive 4TB PCIe Gen4 SSD delivering seamless storage for massive games, 4K video raw footage and virtual machines."),
    ("1TB Gen5 x4 NVMe Next-Gen Ultra M.2 SSD (12,400 MB/s DirectStorage Ready)", 14999, "Gen5 12,400 MB/s", "Next-generation PCIe 5.0 SSD with blazing 12,400 MB/s read speeds, engineered for cutting-edge Intel Core Ultra & AMD 8000/9000 laptops.")
]

for b in ["Samsung Memory", "Western Digital", "Crucial", "Kingston", "Dell"]:
    for title, price, tag, desc in ssd_configs:
        name = f"{b} {title}"
        add_product(
            name=name,
            brand=b,
            category="Laptop Components",
            subcategory="NVMe SSDs",
            price=price,
            tag=tag,
            desc=f"{desc} Certified high-speed storage upgrade for modern gaming laptops and mobile workstations.",
            features=[
                "Extreme Sequential Reads up to 12,400 MB/s for Instant Boot & App Launches",
                "Microsoft DirectStorage Optimized for Next-Gen Gaming Performance",
                "Ultra-Thin M.2 2280 Single-Sided Form Factor Fits All Laptops",
                "Advanced Wear-Leveling and Smart TRIM Support for Longevity"
            ],
            specs={"Interface": "PCIe Gen4 / Gen5 x4 NVMe", "Form Factor": "M.2 2280", "Endurance": "Up to 2400 TBW", "MTBF": "1.5 Million Hours", "Warranty": "5 Years Manufacturer Warranty"},
            inTheBox="1x M.2 NVMe SSD, 1x M.2 Mounting Screw, 1x Thermal Silicon Pad",
            img_key="Laptop SSD",
            warranty="5 Years Brand Warranty",
            compatibleModel="Universal M.2 NVMe Laptop Slot"
        )

# C. LAPTOP REPLACEMENT BATTERIES (20 Items)
battery_configs = [
    ("Dell XPS 15 / 16 (9500 / 9510 / 9520) 86Wh 6-Cell High-Capacity Battery 0-Cycle", 4499, "86Wh 0-Cycle Cell", "Dell XPS 15 86Wh high density pure cobalt 6-cell replacement battery with integrated Texas Instruments protection board."),
    ("HP Omen 16 / Victus 16 83Wh Replacement 4-Cell Li-ion Battery", 3999, "83Wh High Density", "Original spec 83Wh lithium-ion replacement battery for HP Omen gaming laptops, restoring 8+ hours of unplugged performance."),
    ("Lenovo ThinkPad X1 Carbon Gen 9/10/11 57Wh Replacement Battery", 3699, "ThinkPad 57Wh", "Precision 57Wh replacement battery with dual internal cell monitoring for ThinkPad business ultrabooks."),
    ("Lenovo Legion 5 / 5 Pro / 7 80Wh High-Drain Gaming Laptop Battery", 4299, "80Wh Gaming Pack", "80Wh 4-cell high drain replacement pack engineered to sustain high-wattage RTX mobile GPU boost curves without throttling."),
    ("Apple MacBook Pro 16-inch (M1/M2/M3 Pro & Max A2485) 100Wh OEM Battery Assembly", 5999, "100Wh OEM Grade", "Factory 100Wh battery replacement kit for 16\" MacBook Pro with pre-applied adhesive pull tabs and screwdriver kit."),
    ("Apple MacBook Air 13-inch (M1/M2 A2337/A2681) 52.6Wh Original Spec Battery", 4199, "Air 52.6Wh Pack", "High-efficiency 52.6Wh replacement battery restoring all-day 18-hour battery longevity to MacBook Air."),
    ("ASUS ROG Zephyrus G14 / G15 76Wh 4-Cell Replacement Li-Polymer Battery", 3899, "76Wh ROG Battery", "Ultra-thin 76Wh 4-cell lithium-polymer battery module for ASUS Zephyrus compact gaming machines."),
    ("ASUS TUF Gaming A15 / F15 / F17 90Wh Extended Life Replacement Battery", 4199, "90Wh Extended Life", "Huge 90Wh capacity extended battery pack for ASUS TUF series with overcharge and thermal runaway protection ICs."),
    ("Acer Predator Helios 16 / Nitro 5 90Wh High-Capacity Replacement Battery", 3799, "90Wh Predator Pack", "Direct fit 90Wh battery pack with multi-level voltage regulation for Acer gaming laptops."),
    ("MSI Stealth 16 / Raider GE78 99.9Wh Max Flight-Legal Replacement Battery", 4799, "99.9Wh Flight-Legal", "Maximized 99.9Wh battery pack delivering supreme unplugged longevity for MSI enthusiast laptops.")
]

for title, price, tag, desc in battery_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Batteries",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "100% Brand New 0-Cycle Pure Cobalt High Density Cells",
            "Texas Instruments (TI) Multi-Level Smart BMS Protection Board",
            "Over-Voltage, Over-Current, Short-Circuit & Thermal Runaway Protection",
            "Restores Factory-Level All-Day Battery Backup and Quick-Charge Support"
        ],
        specs={"Chemistry": "Lithium-Ion Polymer", "Voltage": "11.4V - 15.4V", "Cell Grade": "Grade A+ 0-Cycle", "Warranty": "1 Year Replacement Warranty"},
        inTheBox="1x Replacement Laptop Battery, 1x Precision Screwdriver Set, 1x Adhesive Removal Tape",
        img_key="Laptop Battery",
        warranty="1 Year Replacement Warranty",
        compatibleModel=title.split("Replacement")[0].strip()
    )

# D. LAPTOP DISPLAY PANELS & OLED ASSEMBLIES (15 Items)
display_configs = [
    ("Dell XPS 16 16.3-inch 4K+ (3840x2400) 120Hz Touch OLED Display Assembly", 14999, "4K 120Hz OLED", "Complete lid and 4K+ 120Hz OLED screen assembly with Corning Gorilla Glass Victus for Dell XPS 16."),
    ("Dell Alienware m16 16.0-inch QHD+ 240Hz 3ms G-SYNC 100% DCI-P3 IPS Display Panel", 9499, "240Hz QHD+ IPS", "Original 240Hz high-refresh matte IPS display panel for Alienware m16 gaming laptops."),
    ("HP Omen 16 16.1-inch QHD 240Hz 3ms 300nits Anti-Glare IPS Display Replacement Panel", 8499, "240Hz QHD Panel", "Zero-dead-pixel guaranteed 240Hz QHD replacement panel for HP Omen 16 gaming laptops."),
    ("HP Spectre x360 14-inch 2.8K (2880x1800) 120Hz OLED Touch Digitizer Assembly", 11999, "2.8K 120Hz OLED Touch", "Factory calibrated 2.8K OLED touch digitizer screen assembly with active pen stylus support."),
    ("Lenovo Legion Pro 7i 16-inch WQXGA (2560x1600) 240Hz 500nits HDR400 Display", 8999, "240Hz 500nits HDR", "Original 16-inch 240Hz WQXGA high-brightness 500-nits IPS panel with factory color calibration."),
    ("Lenovo ThinkPad X1 Carbon 14-inch 2.8K (2880x1800) OLED Non-Touch Matte Display", 9999, "2.8K OLED ThinkPad", "Low-power 2.8K OLED screen assembly with anti-reflective coating for ThinkPad X1 Carbon."),
    ("Apple MacBook Pro 16-inch (Liquid Retina XDR Mini-LED 120Hz ProMotion A2485) Screen Assembly", 26999, "Liquid Retina XDR", "Original complete Liquid Retina XDR 120Hz ProMotion True Tone display lid assembly in Space Gray / Silver."),
    ("Apple MacBook Pro 14-inch (Liquid Retina XDR Mini-LED 120Hz ProMotion A2442) Screen Assembly", 22999, "14\" Mini-LED XDR", "Complete factory display assembly with integrated 1080p FaceTime HD camera and ambient light sensors."),
    ("Apple MacBook Air 15-inch (Liquid Retina True Tone A2941) Display Assembly", 18999, "15\" Liquid Retina", "Factory calibrated 15.3\" Liquid Retina display assembly for MacBook Air M2/M3 with 500 nits brightness."),
    ("ASUS ROG Zephyrus G16 16.0-inch 2.5K 240Hz 0.2ms ROG Nebula OLED Panel", 13499, "ROG Nebula OLED 240Hz", "Ultra-fast 0.2ms response time 240Hz ROG Nebula OLED panel with VESA DisplayHDR True Black 500."),
    ("ASUS TUF Gaming F15 15.6-inch FHD 144Hz IPS Anti-Glare Replacement Screen", 4499, "144Hz FHD IPS", "Drop-in 144Hz Full HD replacement screen panel for ASUS TUF Gaming laptops with 40-pin eDP connector."),
    ("Acer Predator Helios 16 16.0-inch WQXGA 240Hz Mini-LED 1000nits HDR1000 Panel", 12499, "Mini-LED 1000nits", "High-end Mini-LED panel with 1000 nits peak brightness and 1000+ local dimming zones for Predator Helios 16."),
    ("Acer Nitro 5 / 16 15.6-inch FHD 165Hz sRGB 100% IPS Display Screen", 4899, "165Hz IPS Panel", "High color accuracy 165Hz IPS replacement screen with 100% sRGB coverage for Acer Nitro series."),
    ("MSI Titan 18 HX 18.0-inch UHD+ 4K 120Hz Mini-LED 1000nits Display Assembly", 28999, "18\" 4K Mini-LED", "Massive 18-inch 4K 120Hz Mini-LED flagship display assembly for MSI Titan enthusiast systems."),
    ("Samsung Galaxy Book 4 Ultra 16-inch 3K Dynamic AMOLED 2X 120Hz Touch Screen", 15999, "3K Dynamic AMOLED", "Genuine Dynamic AMOLED 2X touch panel with Vision Booster and Corning Gorilla Glass DX.")
]

for title, price, tag, desc in display_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Displays",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "100% Pre-Tested 0-Dead-Pixel Guarantee with Factory Color Calibration",
            "High Refresh Rate (120Hz - 240Hz) with Sub-3ms Smooth Gaming Response",
            "True 100% DCI-P3 / sRGB Wide Color Gamut with HDR Support",
            "Reinforced CNC Bezel with Precision Plug-and-Play eDP Connector"
        ],
        specs={"Panel Type": "OLED / Mini-LED / Fast IPS", "Refresh Rate": "120Hz - 240Hz", "Resolution": "FHD to 4K UHD+", "Condition": "Brand New Factory Sealed OEM", "Warranty": "6 Months Replacement Warranty"},
        inTheBox="1x Complete Display Assembly / Panel, 1x Screen Adhesive Tape Strips, 1x Anti-Static Tool",
        img_key="Laptop Display",
        warranty="6 Months Replacement Warranty",
        compatibleModel=title.split("Display")[0].strip()
    )

# E. LAPTOP KEYBOARDS & TOP CASES (15 Items)
keyboard_configs = [
    ("Dell Alienware m16 / x16 CherryMX Ultra-Low Profile Mechanical Per-Key RGB Keyboard", 4999, "CherryMX Mech RGB", "Genuine Cherry MX ultra-low profile tactile mechanical keyboard with per-key AlienFX RGB lighting."),
    ("Dell XPS 15 (9500 / 9510 / 9520) White / Black Carbon Backlit Keyboard + Palmrest Assembly", 4299, "XPS Backlit Palmrest", "Complete carbon fiber composite top case palmrest with integrated white LED backlit keyboard and fingerprint sensor."),
    ("HP Omen 16 4-Zone RGB Anti-Ghosting Replacement Laptop Keyboard", 2899, "4-Zone RGB", "Tactile gaming keyboard with 4-zone independent RGB backlighting and 26-key rollover anti-ghosting."),
    ("HP Spectre x360 Backlit Island-Style Keyboard Assembly with Precision Touchpad", 3499, "Spectre Island Backlit", "Premium CNC aluminum framed island-style keyboard with whisper-quiet key switches and LED backlight."),
    ("Lenovo ThinkPad X1 Carbon Gen 10/11 Spill-Resistant Backlit TrackPoint Keyboard", 3299, "TrackPoint Backlit", "Iconic ThinkPad ergonomic keyboard featuring the red TrackPoint cap, spill-resistant channels, and crisp scissor-switch travel."),
    ("Lenovo Legion Pro 7i TrueStrike Per-Key RGB Mechanical-Feel Gaming Keyboard", 3899, "TrueStrike Per-Key RGB", "Lenovo Legion TrueStrike keyboard with 1.5mm key travel, 100% anti-ghosting, and Legion Spectrum RGB backlighting."),
    ("Apple MacBook Pro 16-inch (M1/M2/M3 A2485) Magic Keyboard with Touch ID Top Case Assembly", 11999, "Top Case + Magic Key", "Genuine Space Gray top case chassis with installed Magic Keyboard, scissor mechanism, and battery bay."),
    ("Apple MacBook Air 13-inch (M2/M3 A2681) Midnight / Starlight Magic Keyboard Top Case", 9499, "Air M2 Top Case", "Factory Apple unibody top case housing with pre-fitted Magic Keyboard and Touch ID power key."),
    ("ASUS ROG Strix SCAR 18 Per-Key Aura Sync RGB Optical-Mechanical Keyboard", 4699, "Aura Sync Opto-Mech", "Ultra-fast optical-mechanical switches with 0.2ms actuation time and transparent Aura Sync WASD keycaps."),
    ("ASUS TUF Gaming F15 / A15 RGB Backlit Keyboard (Highlighted WASD)", 2499, "TUF RGB Keyboard", "Reinforced military-grade gaming keyboard with overstroke technology and highlighted translucent WASD keys."),
    ("Acer Predator Helios 16 Mini-LED Per-Key RGB Backlit Keyboard", 3499, "Mini-LED Backlit", "Precision PredatorSense per-key Mini-LED keyboard with dedicated Turbo overclock button."),
    ("MSI Titan 18 HX / Raider GE78 SteelSeries Per-Key RGB Mechanical Gaming Keyboard", 5499, "SteelSeries RGB Mech", "SteelSeries co-designed mechanical switch keyboard with independent RGB backlighting for each key."),
    ("Razer Blade 16 Razer Chroma Per-Key RGB Anti-Ghosting Keyboard Module", 5999, "Razer Chroma RGB", "Powered by Razer Chroma RGB with 16.8 million colors and customized tactile dome switches."),
    ("Microsoft Surface Laptop Studio 2 Haptic Touchpad & Backlit Keyboard Palmrest", 8499, "Studio Haptic Top Case", "Full magnesium palmrest assembly with precision haptic touchpad and 1.3mm travel backlit keys."),
    ("Samsung Galaxy Book 4 Pro 360 Full Backlit Keyboard & Glass Touchpad Palmrest", 6499, "Pro 360 Palmrest", "Slim aluminum top cover with quiet island keyboard and extra-large diamond-cut glass touchpad.")
]

for title, price, tag, desc in keyboard_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Keyboards",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "Crisp Scissor / Mechanical Switch Tactile Feedback with Long 10-Million Click Lifespan",
            "Vibrant Per-Key / Multi-Zone RGB & Crisp White LED Backlighting",
            "100% Anti-Ghosting with N-Key Rollover for Accurate Gaming Input",
            "Precision OEM Drop-In Fit with Ribbon Connectors Included"
        ],
        specs={"Switch Type": "Scissor / CherryMX Mechanical", "Backlight": "RGB / White LED", "Condition": "Brand New Factory OEM", "Warranty": "6 Months Replacement Warranty"},
        inTheBox="1x Laptop Keyboard Assembly, 1x Flex Ribbon Cable, 1x Keycap Puller Tool",
        img_key="Laptop Keyboard",
        warranty="6 Months Replacement Warranty",
        compatibleModel=title.split("Keyboard")[0].strip()
    )

# F. DUAL COOLING FANS, HEATPIPES & VAPOR CHAMBERS (15 Items)
cooling_configs = [
    ("Dell Alienware m16 / x16 Cryo-Tech Quad-Fan Liquid Metal Thermal Cooling Heatsink", 3999, "Cryo-Tech Quad Fan", "Alienware Cryo-Tech cooling assembly with Element 31 thermal interface and high-pressure quad cooling fans."),
    ("Dell XPS 15 (9500 / 9510 / 9520) Dual High-RPM CPU + GPU Ultra-Thin Cooling Fans", 1899, "XPS Dual Fan Kit", "Whisper-quiet dual high-RPM cooling fans with carbon liquid crystal polymer blades for XPS 15."),
    ("HP Omen 16 Tempest 12V High-Velocity Dual Cooling Fan Module", 1999, "Tempest 12V Fans", "Omen Tempest cooling fans with 3-sided venting, 5-way airflow, and 12V turbo boost mode."),
    ("HP Victus 15 / 16 Dual Hydro-Bearing CPU/GPU Replacement Cooling Fan Set", 1699, "Victus Dual Fan", "Hydro-bearing low-noise replacement fan pair to eliminate rattling and thermal throttling."),
    ("Lenovo Legion Pro 7i Legion ColdFront 5.0 Vapor Chamber + Dual Turbo Fan Module", 4499, "ColdFront 5.0 Chamber", "Full copper vapor chamber heatsink and ColdFront 5.0 3D blade fans for maximum 175W GPU dissipation."),
    ("Lenovo Legion 5 / 5 Pro Dual Turbo Cooling Fans (Left + Right Pair)", 1899, "Legion Turbo Fan Pair", "High airflow left and right cooling fan set with anti-dust aerodynamic housing."),
    ("Lenovo ThinkPad X1 Carbon Gen 10/11 Owl-Wing Dual Ultra-Quiet Fan Assembly", 2199, "ThinkPad Owl-Wing", "Lenovo Owl-Wing patented ultra-quiet dual micro fans designed for ultrabooks."),
    ("Apple MacBook Pro 16-inch (M1/M2/M3 Max) Left + Right High-Flow Cooling Fan Set", 2899, "MacBook Pro Dual Fan", "Precision balanced low-resonance dual cooling fans for 16\" MacBook Pro M-Series models."),
    ("Apple MacBook Pro 14-inch (M1/M2/M3 Pro) High-Efficiency Thermal Fan Pair", 2499, "14\" Pro Thermal Fan", "OEM matched fan pair designed for high static pressure and silent operation."),
    ("ASUS ROG Strix SCAR 18 Tri-Fan Arc Flow 2.0 Full Surround Copper Heatsink", 4999, "ROG Tri-Fan Heatsink", "Massive full-width copper heatsink and Tri-Fan Arc Flow 2.0 system capable of cooling up to 240W total TDP."),
    ("ASUS ROG Zephyrus G14 / G16 Arc Flow Dual Liquid Crystal Polymer Fans", 2299, "Arc Flow LCP Fans", "84-blade liquid crystal polymer fans with variable thickness to reduce turbulence."),
    ("ASUS TUF Gaming A15 / F15 Dual Dust-Free High-Pressure Cooling Fans", 1799, "TUF Anti-Dust Fan", "TUF self-cleaning dual fan pair with dust tunnels to prevent heatsink clogging."),
    ("Acer Predator Helios 16 5th Gen AeroBlade 3D Metal Fan + Liquid Metal Heatsink", 3899, "AeroBlade 3D Metal", "0.08mm bionic metal blade fans with liquid metal thermal compound contact plate."),
    ("MSI Titan 18 HX / Raider GE78 Cooler Boost 5 Dual Whirlwind Fans + 7 Heatpipes", 4599, "Cooler Boost 5 Module", "Extreme performance cooling module with 7 dedicated copper heatpipes and dual whirlwind fans."),
    ("Razer Blade 16 Custom Vacuum-Sealed Copper Vapor Chamber Heatsink", 5499, "Blade Vapor Chamber", "Ultra-slim vacuum-sealed copper vapor chamber with dual 44-blade high static pressure fans.")
]

for title, price, tag, desc in cooling_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Cooling",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "High-Airflow Hydro / Dual-Ball Bearings for 50,000+ Hours Operational Lifespan",
            "Eliminates Thermal Throttling to Maximize CPU & RTX Mobile GPU Boost Clocks",
            "Precision Balanced Low-Vibration Liquid Crystal Polymer or Bionic Metal Blades",
            "Direct Solder-Free 4-Pin PWM Fan Connector with Automatic Speed Control"
        ],
        specs={"Bearing Type": "Hydro Dynamic / Dual Ball", "Voltage": "5V / 12V DC PWM", "Noise Level": "< 28 dBA", "Warranty": "1 Year Replacement Warranty"},
        inTheBox="1x Left + Right Fan Pair (or Vapor Chamber Heatsink), 1x Thermal Compound Syringe, 1x Screwdriver",
        img_key="Laptop Cooler",
        warranty="1 Year Replacement Warranty",
        compatibleModel=title.split("Cooling")[0].strip()
    )

# G. LAPTOP POWER ADAPTERS & GaN CHARGERS (15 Items)
charger_configs = [
    ("Dell 130W USB-C Type-C Slim Fast Laptop AC Power Adapter (For XPS & Precision)", 3299, "130W USB-C Slim", "Original Dell 130W Type-C laptop adapter delivering 20V/6.5A with integrated cable management clip."),
    ("Dell 240W GaN Barrel 7.4mm Ultra-Slim Power Adapter (For Alienware & G15)", 4499, "240W GaN Alienware", "Next-gen GaN-powered 240W compact power brick for Alienware and Dell G-Series gaming rigs."),
    ("HP 200W Smart AC 4.5mm Blue-Tip Power Adapter (For Omen 16 & Victus)", 3499, "200W HP Blue-Tip", "Original HP 200W smart AC adapter with overvoltage surge suppression and braided AC power cord."),
    ("HP 100W USB-C Power Delivery 3.0 GaN Ultra-Compact Laptop Charger", 2899, "100W GaN USB-C", "Ultra-portable 100W GaN USB-C travel charger supporting PD 3.0 and PPS protocols for Spectre & Envy."),
    ("Lenovo 230W Slim Tip Fast Power Adapter (For Legion Pro 5i/7i & ThinkPad P-Series)", 3999, "230W Slim Tip", "Original Lenovo 230W rectangular slim-tip power supply with Rapid Charge support (0 to 80% in 30 mins)."),
    ("Lenovo 100W USB-C GaN Wall Charger (For ThinkPad X1 Carbon & Yoga 9i)", 2699, "100W GaN ThinkPad", "Compact 100W GaN Type-C charger with foldable AC prongs and 2-meter heavy-duty cable."),
    ("Apple 140W USB-C Dynamic Power Adapter (For MacBook Pro 16-inch M1/M2/M3)", 6499, "140W Apple USB-C", "Apple 140W USB-C Power Adapter with Gallium Nitride efficiency for fast charging 50% in 30 minutes."),
    ("Apple 70W USB-C Compact Power Adapter (For MacBook Air 13/15 & MacBook Pro 14)", 4299, "70W Apple GaN", "Official Apple 70W USB-C Power Adapter for rapid charging MacBook Air and MacBook Pro 14\"."),
    ("ASUS ROG 240W 6.0mm Barrel Plug Compact Gaming Laptop Power Adapter", 4299, "240W ROG Power", "High-efficiency 240W power brick for ASUS ROG Strix and Zephyrus gaming laptops."),
    ("ASUS 100W Type-C ROG GaN Fast Charger (Universal Travel Charger)", 2999, "100W ROG GaN", "ROG branded 100W GaN charger with dual USB-C ports and detachable 2-meter braided cable."),
    ("Acer 230W 5.5mm Barrel High-Output AC Adapter (For Predator Helios 16)", 3899, "230W Predator Power", "Heavy-duty 230W power adapter engineered for peak sustained gaming sessions without power drain."),
    ("MSI 240W Ultra-Slim Gaming Laptop AC Power Adapter (For Raider & Stealth)", 4399, "240W MSI Slim", "Factory replacement 240W slim power brick with reinforced strain relief and ferrite bead filter."),
    ("Razer 280W GaN Ultra-Compact Power Adapter (For Razer Blade 16 & Blade 18)", 6999, "280W Razer GaN", "Incredibly compact 280W GaN power adapter up to 50% smaller than standard 280W bricks."),
    ("Samsung 65W Trio Fast USB-C Power Adapter (For Galaxy Book 4 Series)", 2499, "65W Trio Fast", "Samsung 65W Trio with dual Type-C and USB-A ports to charge Galaxy Book, Galaxy phone and accessories simultaneously."),
    ("Anker Prime 240W 4-Port GaN Desktop Laptop Charging Station", 8999, "240W 4-Port GaN", "Anker Prime GaN station delivering up to 140W single port and 240W total across 3x USB-C and 1x USB-A.")
]

for title, price, tag, desc in charger_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Chargers",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "Gallium Nitride (GaN III) / Smart High-Efficiency Power Semiconductor Architecture",
            "MultiProtect Safety Shield: Over-Voltage, Over-Current, Thermal & Short-Circuit Protection",
            "Certified for Rapid Fast-Charging without Battery Degradation",
            "Includes Heavy-Duty 3-Pin Grounded AC Cord with Reinforced Connectors"
        ],
        specs={"Wattage": "65W - 280W", "Input": "100-240V ~ 50/60Hz Universal", "Safety Standards": "BIS, CE, FCC, RoHS Certified", "Warranty": "1 Year Replacement Warranty"},
        inTheBox="1x Power Adapter Brick, 1x 3-Pin AC Mains Cable, 1x Warranty Booklet",
        img_key="Laptop Charger",
        warranty="1 Year Replacement Warranty",
        compatibleModel=title.split("Adapter")[0].strip()
    )

# H. LAPTOP MOTHERBOARDS & LOGIC BOARDS (12 Items)
mobo_configs = [
    ("Dell XPS 15 (9520) Motherboard (Intel Core i7-12700H + NVIDIA RTX 3050Ti 4GB Unlocked)", 18999, "i7 + RTX 3050Ti", "Factory unlocked genuine Dell XPS 15 motherboard with integrated i7-12700H processor and RTX 3050Ti."),
    ("Dell Alienware m16 R1 Motherboard (Intel Core i9-13900HX + NVIDIA RTX 4080 12GB 175W)", 38999, "i9 + RTX 4080 175W", "Flagship Alienware m16 replacement logic board with 24-core i9-13900HX and full-power 175W RTX 4080 GPU."),
    ("HP Omen 16 (2023) Motherboard (AMD Ryzen 7 7840HS + NVIDIA RTX 4060 8GB 140W TGP)", 22999, "Ryzen 7 + RTX 4060", "Genuine HP Omen 16 mainboard with Zen 4 Ryzen 7 7840HS and 140W Max TGP RTX 4060 graphics."),
    ("HP Victus 16 Motherboard (Intel Core i7-13700H + NVIDIA RTX 4050 6GB)", 16999, "i7 + RTX 4050", "Clean unlocked replacement motherboard for HP Victus 16 with DDR5 dual-slot support."),
    ("Lenovo Legion Pro 7i Gen 8 Motherboard (Intel Core i9-13900HX + RTX 4090 16GB VRAM)", 48999, "i9 + RTX 4090 16GB", "Enthusiast-class Legion Pro 7i mainboard equipped with RTX 4090 16GB GDDR6 and dual Gen4 M.2 slots."),
    ("Lenovo ThinkPad X1 Carbon Gen 11 Logic Board (Intel Core i7-1365U + 32GB LPDDR5 RAM)", 24999, "i7 + 32GB Onboard", "Business-tier ThinkPad X1 logic board with factory soldered 32GB high-speed LPDDR5 RAM and vPro support."),
    ("Apple MacBook Pro 16-inch (M3 Max 16-Core CPU / 40-Core GPU / 36GB Unified Memory A2991) Logic Board", 54999, "M3 Max 36GB Logic", "Original Apple unbonded logic board with M3 Max silicon, 36GB unified memory, and 1TB SSD module."),
    ("Apple MacBook Air 15-inch (M3 8-Core CPU / 10-Core GPU / 16GB Unified Memory A3114) Logic Board", 29999, "M3 16GB Air Logic", "Factory clean Apple MacBook Air 15\" logic board with 16GB unified RAM and clean iCloud unlock."),
    ("ASUS ROG Strix SCAR 18 Motherboard (Intel Core i9-14900HX + NVIDIA RTX 4080 175W)", 42999, "i9-14900HX + RTX 4080", "Cutting-edge 14th Gen Intel Core i9-14900HX ROG mainboard with liquid metal thermal barrier and PCIe Gen5 slot."),
    ("ASUS TUF Gaming A15 Motherboard (AMD Ryzen 7 7735HS + RTX 4060 8GB 140W)", 19999, "Ryzen 7 + RTX 4060", "High durability TUF Gaming motherboard tested for extreme thermal and voltage resilience."),
    ("Acer Predator Helios 16 Motherboard (Intel Core i9-13900HX + RTX 4070 8GB 140W TGP)", 26999, "i9 + RTX 4070", "Full feature Predator Helios motherboard with Turbo overclock profile BIOS and Killer Wi-Fi 6E."),
    ("MSI Raider GE78 HX Motherboard (Intel Core i9-13980HX + RTX 4080 12GB)", 39999, "i9-13980HX + RTX 4080", "Extreme overclocking MSI HX motherboard with MUX switch support and Dynaudio Hi-Res DAC.")
]

for title, price, tag, desc in mobo_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Motherboards",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "100% Tested Unlocked Factory Board with Clean BIOS & No Account Lock",
            "Pre-Installed High Performance CPU & Dedicated NVIDIA GeForce RTX Mobile GPU",
            "Fully Inspected Display, Battery, Wi-Fi, Audio & USB-C Thunderbolt Sockets",
            "Anti-Static ESD Safe Vacuum Moisture-Barrier Packaging"
        ],
        specs={"Condition": "Original OEM Tested & Verified", "Memory Slots": "Dual DDR5 SODIMM / Unified", "Graphics": "NVIDIA GeForce RTX 30/40 Series", "Warranty": "6 Months Replacement Warranty"},
        inTheBox="1x Laptop Motherboard PCB, 1x CPU/GPU Thermal Compound Tube, 1x Static Shield Bag",
        img_key="Laptop Motherboard",
        warranty="6 Months Replacement Warranty",
        compatibleModel=title.split("Motherboard")[0].split("Logic Board")[0].strip()
    )

# I. WI-FI 7, THERMAL PASTES, CHASSIS & ACCESSORIES (35 Items)
misc_configs = [
    ("Intel Killer Wi-Fi 7 BE1750x Tri-Band 320MHz 5.8Gbps M.2 2230 Bluetooth 5.4 Wireless Card", 2999, "Wi-Fi 7 5.8Gbps", "Next-gen Wi-Fi 7 M.2 card delivering 5.8Gbps speeds, 320MHz channel width and ultra-low gaming latency.", "Laptop Wireless"),
    ("Intel Wi-Fi 6E AX210NGW Tri-Band 2.4Gbps M.2 2230 Bluetooth 5.3 Wireless Network Card", 1699, "Wi-Fi 6E AX210", "Gold-standard Wi-Fi 6E wireless card for instant speed and Bluetooth 5.3 upgrades on all laptop models.", "Laptop Wireless"),
    ("Qualcomm FastConnect 7800 Wi-Fi 7 High-Band Simultaneous M.2 Wireless Module", 3499, "Wi-Fi 7 Qualcomm", "High-Band Simultaneous (HBS) Multi-Link technology delivering peak wireless data throughput up to 5.8 Gbps.", "Laptop Wireless"),
    ("MediaTek Wi-Fi 6E MT7922 (RZ616) M.2 2230 PCIe Wireless WLAN Card", 1499, "MediaTek Wi-Fi 6E", "Ultra-fast dual-band Wi-Fi 6E card with Bluetooth 5.2 for ASUS, Acer, and Lenovo laptops.", "Laptop Wireless"),
    ("Honeywell PTM7950 Phase Change Thermal Pad (80x80x0.2mm) High-Performance Laptop Compound", 999, "Honeywell PTM7950", "Original Honeywell PTM7950 phase change thermal pad for maximum heat dissipation without pump-out.", "Laptop Thermal"),
    ("Thermal Grizzly Conductonaut High Performance Liquid Metal Thermal Compound (1.0g)", 1299, "73 W/mK Liquid Metal", "Ultra-high thermal conductivity (73 W/mK) liquid metal compound for enthusiast laptop CPU/GPU overclocking.", "Laptop Thermal"),
    ("Thermal Grizzly Kryonaut Extreme High-End Thermal Grease (2g Syringe)", 1199, "14.2 W/mK Kryonaut", "Specially designed for extreme gaming loads and sub-zero thermal dissipation with 14.2 W/mK conductivity.", "Laptop Thermal"),
    ("Arctic MX-6 Extreme Carbon Micro-Particle Thermal Paste (4g Syringe + Spatula)", 699, "Arctic MX-6 4g", "High viscosity carbon micro-particle thermal paste engineered to eliminate thermal throttling.", "Laptop Thermal"),
    ("K5 PRO High Viscosity Thermal Paste for Laptop GPU VRAM & VRM Phase Chips (20g)", 899, "K5 PRO VRAM Paste", "Specialized gummy thermal paste designed for laptop GPU VRAM chips and power delivery MOSFETs.", "Laptop Thermal"),
    ("Upsiren U6 PRO Thermal Putty High Thermal Conductivity (12.8 W/mK, 50g)", 1499, "12.8 W/mK Putty", "Non-conductive gap-filling thermal putty replacing dried-out thermal pads on high-TDP laptop heatsinks.", "Laptop Thermal"),
    ("Dell XPS 15 (9500 / 9510 / 9520) Left + Right CNC Aluminum Display Hinge Set", 1299, "XPS 15 Hinges", "Reinforced precision friction hinge set to repair loose or wobbly display screens on Dell XPS 15.", "Laptop Chassis"),
    ("HP Omen 16 / Victus 16 Left & Right Reinforced Steel LCD Display Hinges Pair", 1199, "Omen 16 Hinges", "Heavy-duty steel replacement hinges tested for 20,000+ opening and closing cycles without fatigue.", "Laptop Chassis"),
    ("Lenovo Legion 5 / 5 Pro / 7 Screen Hinge Bracket Kit (Left + Right)", 1299, "Legion Hinge Kit", "Factory reinforced screen hinges to permanently fix cracked or stiff Legion display joints.", "Laptop Chassis"),
    ("ASUS ROG Zephyrus G14 / G16 ErgoLift Display Hinge Mechanism Pair", 1399, "ROG ErgoLift Hinges", "ErgoLift hinge pair that tilts the keyboard for better ergonomics and enhanced cooling airflow.", "Laptop Chassis"),
    ("Apple MacBook Pro 16-inch (A2485) MagSafe 3 DC-In Power Charging Port Flex Cable", 1499, "MagSafe 3 Port", "Original MagSafe 3 magnetic charging port flex module for MacBook Pro 16-inch.", "Laptop Chassis"),
    ("Apple MacBook Air 13-inch (M2/M3 A2681) MagSafe 3 Fast Charging Socket Board", 1299, "Air MagSafe 3", "Genuine Apple MagSafe 3 DC-In board flex for rapid magnetic fast charging.", "Laptop Chassis"),
    ("Dell XPS 15 USB-C Thunderbolt 4 Daughterboard I/O Audio Board Flex", 1799, "XPS I/O Board", "Factory replacement I/O daughterboard with dual Thunderbolt 4 ports, SD card reader and 3.5mm jack.", "Laptop Chassis"),
    ("Lenovo Legion Pro 7i USB-C & Power DC Jack Rear I/O Board Assembly", 1999, "Legion Rear I/O", "Replacement rear I/O PCB containing Gigabit LAN, USB-C DisplayPort and DC power input jack.", "Laptop Chassis"),
    ("ASUS ROG Strix SCAR 18 Audio Combo Jack & USB 3.2 Gen2 Side Daughter Board", 1499, "ROG Side I/O Board", "Genuine side daughterboard flex assembly with high-speed USB ports and Hi-Res audio DAC socket.", "Laptop Chassis"),
    ("HP Omen 16 Power Button Board & Indicator LED Flex Cable", 899, "Omen Power Board", "Replacement tactile power switch circuit board with status LED and ribbon flex connector.", "Laptop Chassis"),
    ("Dell XPS 15 Precision Glass Multi-Touch Haptic Touchpad Module", 2199, "Glass Touchpad", "Extra-large frosted glass multi-touch precision touchpad with smooth gesture recognition.", "Laptop Chassis"),
    ("Lenovo ThinkPad X1 Carbon Gen 10 Glass TrackPoint Multi-Gesture Touchpad", 2499, "ThinkPad Glass Touchpad", "Genuine ThinkPad precision glass touchpad with dedicated physical three-button TrackPoint clickers.", "Laptop Chassis"),
    ("Apple MacBook Pro 16-inch (A2485) Force Touch Haptic Feedback Trackpad Assembly", 4999, "Force Touch Trackpad", "Genuine Force Touch trackpad with taptic engine feedback and pressure sensing capabilities.", "Laptop Chassis"),
    ("ASUS ROG Zephyrus G16 Glass Touchpad with 240Hz Smooth Response", 2299, "ROG Glass Trackpad", "Smooth glass surface touchpad with seamless edge rejection and multi-touch Windows Precision gestures.", "Laptop Chassis"),
    ("Universal 120-in-1 Precision Laptop & Electronics Teardown Screwdriver Tool Kit", 1199, "120-in-1 Pro Tool Kit", "Professional magnetic S2 steel repair kit with Torx, Pentalobe, Phillips, spudgers, and suction cups.", "Laptop Thermal"),
    ("ESD Anti-Static Wrist Strap + Grounding Cord for Laptop Disassembly & Repair", 399, "Anti-Static Strap", "Elastic ESD wristband with alligator clip to protect sensitive laptop motherboards from static discharge.", "Laptop Thermal"),
    ("Anti-Static ESD Safe Heat-Resistant Silicone Magnetic Soldering Mat (45x30cm)", 899, "ESD Silicone Mat", "Heat-resistant up to 500°C magnetic repair mat with built-in component compartments and screw organizers.", "Laptop Thermal"),
    ("Dell XPS 15 CNC Machined Aerospace Aluminum Bottom Base Cover Door with Dust Filter", 2799, "XPS Bottom Cover", "Precision CNC aluminum bottom chassis shell with laser-cut intake ventilation grilles and rubber feet.", "Laptop Chassis"),
    ("HP Omen 16 Bottom Case Shell with Raised Rubber Feet & Air Intake Mesh", 2299, "Omen Bottom Shell", "Factory replacement bottom cover with high-flow dust filtration mesh to prevent debris buildup.", "Laptop Chassis"),
    ("Lenovo Legion Pro 7i Magnesium-Aluminum Bottom Enclosure Chassis Door", 2599, "Legion Bottom Cover", "Rigid magnesium-aluminum lower housing providing structural strength and optimal thermal airflow.", "Laptop Chassis"),
    ("Apple MacBook Pro 16-inch Unibody Aluminum Bottom Case Cover Plate (Space Gray)", 3899, "MacBook Bottom Plate", "Genuine unibody aluminum bottom plate with laser-etched model serial and ventilation exhausts.", "Laptop Chassis"),
    ("Dell Alienware m16 Clear Glass AlienFX Stadium Rear Lighting Ring Bezel", 1899, "Alienware Lighting Ring", "Iconic AlienFX stadium lighting acrylic ring diffuser for rear I/O thermal shelf.", "Laptop Chassis"),
    ("Universal Laptop Internal Stereo Subwoofer & High-Frequency Tweeter Speaker Kit", 1499, "Hi-Res Laptop Speakers", "Deep bass acoustic speaker chambers with high-frequency tweeters for crisp dialogue and gaming immersion.", "Laptop Chassis"),
    ("Laptop Screen Front Bezel Trim Frame with Pre-Applied 3M Adhesive Tape (15.6\" & 16\")", 899, "Screen Bezel Trim", "Precision molded replacement front display bezel with camera shutter cutout and microphone holes.", "Laptop Chassis"),
    ("Replacement Anti-Slip Silicone Rubber Feet Strip Set for Gaming Laptops (Pack of 4)", 349, "Rubber Feet Strips", "High-grip elevated rubber footpads to improve laptop desk grip and increase underneath air intake clearance.", "Laptop Chassis")
]

for title, price, tag, desc, img_key in misc_configs:
    brand = title.split()[0]
    add_product(
        name=title,
        brand=brand,
        category="Laptop Components",
        subcategory="Laptop Accessories & Spares",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "100% Genuine OEM Replacement / Upgrade Specification",
            "Precision Engineered for Seamless Fit and Maximum Thermal / Mechanical Durability",
            "Includes Necessary Screws, Flex Cables & Thermal Accessories",
            "Rigorous Quality Testing before Packaging and Dispatch"
        ],
        specs={"Category": "Laptop Spares & Upgrade", "Condition": "Brand New", "Warranty": "6 Months to 1 Year Warranty"},
        inTheBox="1x Component Unit, 1x Protective Anti-Static Pack",
        img_key=img_key,
        warranty="1 Year Warranty",
        compatibleModel=title.split("(")[0].strip()
    )

print(f"Generated {len([p for p in all_products if p['category']=='Laptop Components'])} Laptop Components!")

# =========================================================================
# 3. COMPLETE LAPTOPS & NOTEBOOKS (15 Flagship Models)
# =========================================================================

laptop_models = [
    ("Apple MacBook Pro 16-inch (M3 Max 16-Core CPU, 40-Core GPU, 36GB Unified RAM, 1TB SSD, Liquid Retina XDR)", "Apple", 349900, "M3 Max Powerhouse", "The ultimate pro laptop with industry-leading M3 Max silicon, 22-hour battery life and stunning Liquid Retina XDR display.", "Laptop"),
    ("Apple MacBook Air 15-inch (M3 8-Core CPU, 10-Core GPU, 16GB Unified RAM, 512GB SSD, Liquid Retina)", "Apple", 154900, "M3 Ultra-Slim", "Impossibly thin 15-inch MacBook Air with all-day 18-hour battery life, 500 nits Liquid Retina display and silent fanless design.", "Laptop"),
    ("Dell XPS 16 (Intel Core Ultra 9 185H, NVIDIA RTX 4070 8GB, 32GB LPDDR5X, 1TB SSD, 16.3\" 4K+ 120Hz OLED Touch)", "Dell", 289990, "4K OLED Creator", "Futuristic CNC aluminum design with invisible haptic glass touchpad, touch function row and vibrant 4K OLED display.", "Laptop"),
    ("Dell Alienware m16 R2 (Intel Core Ultra 9 185H, NVIDIA RTX 4070 140W, 32GB DDR5, 1TB SSD, 16\" QHD+ 240Hz)", "Dell", 219990, "Alienware Stealth", "Redesigned compact Alienware chassis with Stealth Mode, Cryo-tech cooling and ultra-responsive 240Hz QHD+ gaming screen.", "Laptop"),
    ("ASUS ROG Zephyrus G16 (Intel Core Ultra 9 185H, NVIDIA RTX 4080 12GB 145W, 32GB LPDDR5X, 2TB SSD, 2.5K OLED 240Hz)", "ASUS", 299990, "ROG OLED 240Hz", "Ultra-sleek 1.85kg CNC aluminum gaming laptop with world-first 2.5K 240Hz ROG Nebula OLED display and Slash Lighting.", "Laptop"),
    ("ASUS ROG Strix SCAR 18 (Intel Core i9-14900HX, NVIDIA RTX 4090 16GB 175W, 32GB DDR5, 2TB SSD, 18\" 2.5K 240Hz Mini-LED)", "ASUS", 379990, "18\" RTX 4090 Monster", "Uncompromised desktop replacement with 18-inch Mini-LED 1100 nits ROG Nebula HDR panel and 175W RTX 4090 power.", "Laptop"),
    ("Lenovo Legion Pro 7i Gen 9 (Intel Core i9-14900HX, NVIDIA RTX 4090 16GB 175W, 32GB DDR5, 2TB SSD, 16\" 240Hz WQXGA)", "Lenovo", 339990, "Legion Pro 7i AI", "Powered by Lenovo LA-2 AI tuning chip, full-power 175W RTX 4090, Legion ColdFront 5.0 vapor chamber and 240Hz display.", "Laptop"),
    ("Lenovo ThinkPad X1 Carbon Gen 12 (Intel Core Ultra 7 155H, 32GB LPDDR5X, 1TB SSD, 14\" 2.8K 120Hz OLED)", "Lenovo", 224990, "ThinkPad Flagship", "Legendary ultrabook redefined with carbon fiber chassis, Communications Bar with 8MP webcam, and 2.8K OLED display.", "Laptop"),
    ("HP Omen Transcend 16 (Intel Core i9-14900HX, NVIDIA RTX 4070 8GB, 32GB DDR5, 1TB SSD, 16\" 240Hz OLED)", "HP", 209990, "Omen Transcend OLED", "Slim magnesium-aluminum gaming laptop featuring a breathtaking 240Hz OLED display and tempest cooling.", "Laptop"),
    ("Acer Predator Helios 18 (Intel Core i9-14900HX, NVIDIA RTX 4080 12GB 175W, 32GB DDR5, 2TB SSD, 18\" 250Hz Mini-LED)", "Acer", 279990, "Predator 18\" Mini-LED", "Massive 18-inch Mini-LED powerhouse with MagKey 3.0 swappable mechanical WASD keys and 5th Gen AeroBlade 3D fans.", "Laptop"),
    ("MSI Titan 18 HX A14V (Intel Core i9-14900HX, NVIDIA RTX 4090 16GB 175W, 64GB DDR5, 4TB SSD, 18\" 4K 120Hz Mini-LED)", "MSI", 499990, "Titan 18 HX Apex", "The apex of mobile computing: 4K 120Hz Mini-LED, Cherry MX mechanical keyboard, 270W total system power and RGB haptic touchpad.", "Laptop"),
    ("Samsung Galaxy Book 4 Ultra (Intel Core Ultra 9 185H, NVIDIA RTX 4070 8GB, 32GB LPDDR5X, 1TB SSD, 16\" 3K 120Hz AMOLED Touch)", "Samsung", 249990, "Galaxy Ecosystem Pro", "Intelligent AI PC with 3K Dynamic AMOLED 2X touchscreen, anti-reflective coating, and seamless Galaxy multi-device continuity.", "Laptop"),
    ("Razer Blade 16 (Intel Core i9-14900HX, NVIDIA RTX 4090 16GB 175W, 32GB DDR5, 2TB SSD, Dual-Mode Mini-LED 4K 120Hz / FHD 240Hz)", "Razer", 419990, "Dual-Mode Mini-LED", "World-first dual-mode Mini-LED display switching between creator 4K 120Hz and esports FHD+ 240Hz in a CNC unibody.", "Laptop"),
    ("Microsoft Surface Laptop Studio 2 (Intel Core i7-13700H, NVIDIA RTX 4060 8GB, 32GB RAM, 1TB SSD, 14.4\" PixelSense Touch)", "Microsoft", 269990, "Surface Transformable", "Dynamic woven hinge transforms seamlessly from high-performance laptop to creative studio canvas with Surface Slim Pen 2.", "Laptop"),
    ("LG Gram Pro 16 (Intel Core Ultra 7 155H, NVIDIA RTX 3050 4GB, 32GB LPDDR5X, 1TB SSD, 16\" 144Hz WQXGA IPS, 1.19kg)", "LG", 179990, "1.19kg Ultra-Light", "World's lightest 16-inch laptop with dedicated NVIDIA graphics, military-spec durability and massive 77Wh battery.", "Laptop")
]

for name, brand, price, tag, desc, img_key in laptop_models:
    add_product(
        name=name,
        brand=brand,
        category="Laptops & Notebooks",
        subcategory="Flagship Laptops",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "100% Brand New Factory Sealed Box Pack with 1-Year Official Manufacturer Warranty",
            "Cutting-Edge High-Performance Processor with Dedicated GPU / Neural AI NPU",
            "High Refresh Rate AMOLED / Mini-LED / Fast IPS Display with 100% Color Accuracy",
            "All-Day High Density Battery with Rapid Fast Power Delivery Support"
        ],
        specs={"Brand": brand, "Display": name.split(",")[-1].strip(), "Condition": "Brand New Factory Sealed", "Warranty": "1 Year Official Manufacturer Warranty across all Authorized Service Centers"},
        inTheBox=f"1x {name.split('(')[0].strip()} Laptop, 1x Fast Power Adapter, 1x Power Cord, 1x User Manual & Warranty Card",
        img_key=img_key,
        warranty="1 Year Official Brand Warranty",
        compatibleModel=name.split("(")[0].strip()
    )

print(f"Generated {len([p for p in all_products if p['category']=='Laptops & Notebooks'])} Laptops!")

# =========================================================================
# 4. PERIPHERALS: BUDS (TWS), HEADSETS, CHARGERS, SMARTWATCHES
# =========================================================================

# A. BUDS / TWS EARBUDS (12 Items)
buds_list = [
    ("Apple AirPods Pro 2 (USB-C MagSafe Charging Case, Active Noise Cancellation, H2 Chip)", "Apple", 24900, "Pro ANC Master", "Featuring 2x more Active Noise Cancellation, Adaptive Audio, Transparency mode, and USB-C MagSafe case with Precision Finding.", "Buds"),
    ("Samsung Galaxy Buds3 Pro (Blade Lights, 24-bit Hi-Fi Audio, Adaptive Noise Control)", "Samsung", 19999, "Blade Lights Hi-Fi", "Next-gen angled design with iconic Blade Lights, dual dynamic drivers, planar tweeters, and AI-powered voice detect.", "Buds"),
    ("Sony WF-1000XM5 Industry Leading Noise Canceling True Wireless Earbuds (LDAC, Hi-Res)", "Sony", 24990, "Best ANC in Class", "Dual feedback microphones and Integrated Processor V2 deliver unparalleled silence and crystal-clear call quality.", "Buds"),
    ("Bose QuietComfort Ultra Earbuds (Bose Immersive Audio, CustomTune Technology)", "Bose", 25900, "Spatial Immersive ANC", "Groundbreaking spatial audio creates an acoustic sweet spot wherever you listen, paired with world-class noise cancellation.", "Buds"),
    ("OnePlus Buds Pro 3 (Dynaudio Co-Created Dual Drivers, 50dB Smart Adaptive ANC)", "OnePlus", 11999, "Dynaudio Acoustic", "Dual DACs with 11mm woofer + 6mm tweeter co-created with Dynaudio, 50dB smart ANC, and 43 hours battery life.", "Buds"),
    ("Sennheiser Momentum True Wireless 4 (Lossless Audio, Auracast & LE Audio, 30h Playtime)", "Sennheiser", 24990, "Audiophile Lossless", "Engineered for pure audiophile sound with TrueResponse transducer system, aptX Lossless, and copper weave charging case.", "Buds"),
    ("Nothing Ear (2024) (11mm Ceramic Driver, 45dB Smart ANC, Hi-Res LHDC 5.0 Wireless)", "Nothing", 11999, "Transparent Ceramic", "Signature transparent enclosure with custom ceramic driver for punchy bass and pristine treble clarity.", "Buds"),
    ("JBL Live Beam 3 (Smart Charging Case with 1.45\" Touch Display, True Adaptive ANC)", "JBL", 13999, "Smart Screen Case", "Control music, ANC modes, and phone calls directly from the innovative full-color touchscreen smart case.", "Buds"),
    ("Realme Buds Air 6 Pro (50dB Active Noise Cancellation, Dual Dynamic Drivers, LDAC)", "Realme", 4999, "50dB Deep ANC", "Flagship-tier 50dB deep noise cancellation with dual coaxial drivers and 40-hour long-lasting battery.", "Buds"),
    ("boAt Airdopes 800 (Dolby Audio Spatial Sound, 40h Playtime, AI-ENx Quad Mics)", "boAt", 2499, "Dolby Audio Spatial", "Powered by Dolby Audio for cinematic spatial surround sound with quad AI microphones for clear calls.", "Buds"),
    ("Beats Studio Buds + (Transparent Design, Custom Acoustic Platform, 36h Playtime)", "Beats", 16900, "Iconic Transparent", "Custom Beats acoustic architecture with powerful balanced sound and enhanced compatibility with iOS & Android.", "Buds"),
    ("Google Pixel Buds Pro 2 (Tensor A1 Chip, Silent Seal 2.0, 48kHz Hi-Res Audio)", "Google", 22900, "Tensor A1 Smart ANC", "First buds powered by Google Tensor A1 chip for ultra-fast noise cancellation and Gemini Live voice interactions.", "Buds")
]

for name, brand, price, tag, desc, img_key in buds_list:
    add_product(
        name=name,
        brand=brand,
        category="Buds & TWS",
        subcategory="TWS Earbuds",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "Hybrid Active Noise Cancellation (ANC) with Crystal Transparency Mode",
            "Audiophile Dynamic Drivers with Hi-Res LDAC / AAC Audio Codec Support",
            "Quad-Mic AI Noise Reduction for Crystal Clear Hands-Free Calling",
            "Fast Charging Support: 10 Mins Charge Provides Up to 5 Hours Playback"
        ],
        specs={"Driver Size": "10mm - 12mm Titanium/Ceramic", "Battery Life": "Up to 45 Hours with Case", "Water Resistance": "IPX4 / IP54 Sweat Proof", "Bluetooth": "v5.3 / v5.4 Dual Connect", "Warranty": "1 Year Official Brand Warranty"},
        inTheBox="1x TWS Earbuds Pair, 1x Wireless Charging Case, 3x Silicone Ear Tips (S/M/L), 1x Type-C Cable, 1x Manual",
        img_key=img_key,
        warranty="1 Year Brand Warranty",
        compatibleModel="Universal Bluetooth iOS & Android"
    )

# B. HEADSETS & OVER-EAR HEADPHONES (12 Items)
headset_list = [
    ("Sony WH-1000XM5 Wireless Noise Canceling Headphones (Auto NC Optimizer, 30h Battery)", "Sony", 29990, "Flagship King ANC", "Two processors control 8 microphones for unprecedented noise cancellation and magnificent high-resolution sound.", "Headsets"),
    ("Bose QuietComfort Ultra Headphones (Spatial Audio, CustomTune, Ultra-Comfort Plush)", "Bose", 35900, "Ultra Spatial Comfort", "Immersive audio breaks acoustic boundaries with world-class noise cancellation and luxurious protein leather earcups.", "Headsets"),
    ("Apple AirPods Max (USB-C Charging, Computational Audio, Spatial Audio with Head Tracking)", "Apple", 59900, "Apple Acoustic Apex", "High-fidelity audio with custom acoustic design, Apple H1 chips, active noise cancellation, and breathable mesh canopy.", "Headsets"),
    ("Sennheiser Momentum 4 Wireless Headphones (Audiophile 42mm Drivers, 60h Battery)", "Sennheiser", 27990, "60-Hour Battery Beast", "Audiophile-inspired 42mm transducer system delivering brilliant dynamics, clarity, and unmatched 60-hour playback.", "Headsets"),
    ("Razer BlackShark V2 Pro Wireless Esports Gaming Headset (HyperClear Super Wideband Mic)", "Razer", 19999, "Esports Legend Mic", "The definitive wireless headset for competitive esports with broadcast-grade mic and TriForce Titanium 50mm drivers.", "Headsets"),
    ("HyperX Cloud III Wireless Gaming Headset (120-Hour Battery, DTS Headphone:X Spatial)", "HyperX", 14990, "120-Hour Ultra Battery", "Legendary HyperX memory foam comfort with an astounding 120-hour battery life and re-engineered 53mm angled drivers.", "Headsets"),
    ("SteelSeries Arctis Nova Pro Wireless Headset (Multi-System Connect, Active Noise Cancellation)", "SteelSeries", 36999, "Infinity Battery System", "Nova Pro Acoustic System with dual-wireless 2.4GHz + Bluetooth, active noise cancellation, and hot-swap battery base.", "Headsets"),
    ("Logitech G PRO X 2 LIGHTSPEED Wireless Gaming Headset (50mm Graphene Drivers, Blue VO!CE)", "Logitech", 24995, "PRO-G Graphene Drivers", "Revolutionary 50mm pure graphene audio drivers engineered for pro tournament gamers with Blue VO!CE microphone.", "Headsets"),
    ("Audio-Technica ATH-M50xBT2 Wireless Professional Studio Monitor Headphones (LDAC)", "Audio-Technica", 18990, "Studio Reference Sound", "Legendary M50x studio sonic signature with dual beamforming mics, LDAC wireless support, and 50 hours battery.", "Headsets"),
    ("Corsair HS80 MAX Wireless Spatial Audio Gaming Headset (Dolby Atmos, Broadcast Mic)", "Corsair", 16999, "Dolby Atmos Spatial", "High-fidelity 24-bit/96kHz audio with Dolby Atmos spatial surround and omnidirectional broadcast-grade mic.", "Headsets"),
    ("JBL Tour ONE M2 (True Adaptive Noise Cancelling, Hi-Res Certified 40mm Drivers, 50h)", "JBL", 19999, "JBL Pro Sound", "Smart Ambient and True Adaptive ANC with 4-mic crystal clear call technology and customizable Personi-Fi 2.0 sound.", "Headsets"),
    ("Marshall Major V Wireless Bluetooth Headphones (100+ Hours Playtime, Rugged Foldable)", "Marshall", 14999, "100+ Hours Classic Rock", "Iconic Marshall vintage textured vinyl design delivering roaring bass and over 100 hours of wireless playback.", "Headsets")
]

for name, brand, price, tag, desc, img_key in headset_list:
    add_product(
        name=name,
        brand=brand,
        category="Headsets & Headphones",
        subcategory="Over-Ear Headphones",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "Studio-Grade 40mm - 53mm Dynamic Drivers with Hi-Res Audio Certification",
            "Multi-Mic Hybrid Active Noise Cancellation with Transparency Awareness",
            "Ultra-Plush Memory Foam Ear Cushions for Fatigue-Free All-Day Listening",
            "Dual Mode Connectivity: Ultra-Low Latency 2.4GHz / Bluetooth 5.3 + 3.5mm Aux"
        ],
        specs={"Driver Diameter": "40mm - 53mm", "Frequency Response": "10Hz - 40,000Hz", "Battery Life": "30 to 120 Hours Playtime", "Weight": "250g - 380g", "Warranty": "1 Year Manufacturer Warranty"},
        inTheBox="1x Over-Ear Headset, 1x Hard Travel Case, 1x 3.5mm Audio Cable, 1x USB-C Fast Charging Cable, 1x User Guide",
        img_key=img_key,
        warranty="1 Year Official Warranty",
        compatibleModel="PC, Mac, PlayStation 5, Xbox, Switch & Smartphones"
    )

# C. FAST CHARGERS & POWER (10 Items)
charger_periph_list = [
    ("Anker Prime 100W GaN 3-Port Ultra-Fast Wall Charger (2x USB-C + 1x USB-A, PowerIQ 4.0)", "Anker", 5999, "100W GaN Prime", "Ultra-compact 100W GaN charger capable of powering a 16\" MacBook Pro, iPad Pro, and iPhone simultaneously with ActiveShield 2.0.", "Chargers"),
    ("UGREEN Nexode 140W Multi-Port GaN Desktop Fast Charger (PD 3.1, GaNFast Tech, 4-Port)", "UGREEN", 8499, "140W Desktop GaN", "Next-gen PD 3.1 protocol charger delivering a single 140W port for fast-charging flagship laptops and tablets.", "Chargers"),
    ("Apple 140W USB-C Dynamic Power Adapter (Official Fast Charger)", "Apple", 6499, "140W Apple GaN", "Genuine Apple 140W power adapter optimized for charging MacBook Pro 16\" from 0% to 50% in 30 minutes.", "Chargers"),
    ("Samsung 65W Trio Power Adapter (Type-C 65W + Type-C 25W + USB-A 15W Super Fast Charging)", "Samsung", 2999, "65W Trio Samsung", "Charge three devices at once with Super Fast Charging 2.0 for Galaxy smartphones, Galaxy Books, and accessories.", "Chargers"),
    ("Belkin BoostCharge Pro 3-in-1 MagSafe 15W Fast Wireless Charging Stand", "Belkin", 13999, "15W MagSafe 3-in-1", "Premium stainless steel stand delivering official 15W MagSafe wireless charging for iPhone, Apple Watch, and AirPods.", "Chargers"),
    ("Baseus Blade 100W Ultra-Slim Laptop Power Bank (20,000mAh, 4-Port Digital Display, 18mm Slim)", "Baseus", 6999, "100W 20000mAh Slim", "Ultra-thin 18mm laptop power bank slipping effortlessly into backpacks with high-visibility digital power metering display.", "Chargers"),
    ("SPEK GaN III Pro 120W Dual Type-C + USB-A Turbo Fast Charger with Foldable Pins", "SPEK", 3499, "SPEK 120W Turbo", "Our signature GaN III Pro high-efficiency 120W fast power brick with cool-running semiconductor architecture.", "Chargers"),
    ("Anker 737 Power Bank (PowerCore 24K, 140W Two-Way Smart Digital Display Output)", "Anker", 11999, "140W Smart 24K", "Equipped with the latest Power Delivery 3.1 and bi-directional technology to quickly recharge the power bank or power laptops.", "Chargers"),
    ("UGREEN 240W Zinc-Alloy Braided USB-C to USB-C 5A Fast Charging Cable (2-Pack, 2M)", "UGREEN", 1499, "240W 48V/5A Cable", "Indestructible zinc-alloy braided cable supporting up to 240W Power Delivery and 480Mbps data sync transfer.", "Chargers"),
    ("Spigen ArcField 15W Qi-Certified Fast Wireless Charging Pad with AirBoost Tech", "Spigen", 1999, "15W Qi Wireless", "Non-slip rubberized fast wireless charging pad with intelligent thermal protection and case-friendly transmission.", "Chargers")
]

for name, brand, price, tag, desc, img_key in charger_periph_list:
    add_product(
        name=name,
        brand=brand,
        category="Fast Chargers & Power",
        subcategory="Chargers & Powerbanks",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "Gallium Nitride (GaN III) Ultra-Efficient Fast Charging Circuitry",
            "Multi-Port Simultaneous Fast Charging with Intelligent Smart Power Allocation",
            "Active Thermal Monitoring Prevents Overheating and Battery Strain",
            "Universal Protocol Compatibility: PD 3.1, QC 4.0+, PPS, AFC & SuperVOOC"
        ],
        specs={"Max Output": "65W - 240W", "Ports": "USB-C & USB-A Fast Ports", "Certification": "BIS, CE, FCC, RoHS Certified", "Warranty": "1 Year Replacement Warranty"},
        inTheBox="1x Fast Charger / Powerbank Unit, 1x Braided Cable, 1x User Manual",
        img_key=img_key,
        warranty="1 Year Brand Warranty",
        compatibleModel="Universal Type-C Laptops, Tablets & Smartphones"
    )

# D. SMARTWATCHES & WEARABLES (12 Items)
smartwatch_list = [
    ("Apple Watch Ultra 2 (Titanium Case, 3000 nits Always-On Retina OLED, Precision Dual GPS)", "Apple", 89900, "Titanium Ultra 2", "The ultimate sports and adventure watch with aerospace titanium casing, 36-hour battery, Action button, and 100m water resistance.", "Smartwatches"),
    ("Apple Watch Series 10 (Thinnest Design, Wide-Angle OLED Display, Sleep Apnea Detection)", "Apple", 46900, "Series 10 OLED", "Re-engineered with a 10% thinner profile, 40% brighter wide-angle OLED screen, fast charging, and depth gauge.", "Smartwatches"),
    ("Samsung Galaxy Watch Ultra (Grade 4 Titanium, 100m Water Resistance, Dual-Frequency GPS, LTE)", "Samsung", 59999, "Galaxy Watch Ultra", "Built for extreme conditions with rugged cushion design, multi-day battery life, BioActive Sensor, and Galaxy AI coaching.", "Smartwatches"),
    ("Samsung Galaxy Watch 7 (BioActive Sensor 2.0, Energy Score, AI Health Insights, Super AMOLED)", "Samsung", 29999, "Galaxy Watch 7", "Sleek floating glass design with dual-frequency GPS, Energy Score, and comprehensive wellness monitoring.", "Smartwatches"),
    ("Garmin Fenix 8 Solar Sapphire Multisport GPS Watch (Solar Charging, TopoActive Maps, 28 Days)", "Garmin", 86990, "28-Day Solar Sapphire", "Premium multisport GPS smartwatch with solar charging lens, built-in speaker and mic, sensor guard, and TopoActive maps.", "Smartwatches"),
    ("Garmin Forerunner 965 Premium Running & Triathlon GPS Watch (1.4\" AMOLED, Titanium Bezel)", "Garmin", 64990, "Forerunner AMOLED", "Brilliant 1.4-inch AMOLED touchscreen with lightweight titanium bezel, training readiness metrics, and full-color mapping.", "Smartwatches"),
    ("Google Pixel Watch 3 (45mm Actua Display 2000 nits, Fitbit Readiness & Cardio Load)", "Google", 39900, "Pixel Actua 2000 nits", "Bigger, brighter Actua display with custom Fitbit performance tools, Loss of Pulse Detection, and seamless Google integration.", "Smartwatches"),
    ("OnePlus Watch 2R (Dual-Engine Architecture, Wear OS 4, 100-Hour Battery, Snapdragon W5)", "OnePlus", 17999, "100-Hour Dual Engine", "Powered by Snapdragon W5 + BES2700 dual-chipset delivering full Google Wear OS 4 and an astounding 100-hour battery life.", "Smartwatches"),
    ("Amazfit Cheetah Pro (Premium Titanium Bezel, MaxTrack Dual-Band GPS, AI Running Coach)", "Amazfit", 24999, "Titanium Marathon AI", "Specialized running watch with MaxTrack circularly-polarized dual-band GPS antenna, AI coaching, and offline maps.", "Smartwatches"),
    ("Noise ColorFit Ultra 3 (1.96\" AMOLED Always-On Display, Metallic Finish, Bluetooth Calling)", "Noise", 3499, "1.96\" AMOLED Calling", "Vibrant 1.96-inch Always-On AMOLED screen with Tru Sync Bluetooth calling and comprehensive 24/7 heart & SpO2 tracking.", "Smartwatches"),
    ("boAt Wave Fury (1.83\" HD Display, Bluetooth Calling, 50+ Sports Modes, IP68 Waterproof)", "boAt", 1799, "Value HD Calling", "Affordable fitness companion with premium zinc-alloy frame, one-tap Bluetooth calling, and multiple sports tracking.", "Smartwatches"),
    ("Amazfit T-Rex 3 (Military-Grade Rugged Smartwatch, Dual-Band Offline Maps, 27 Days Battery)", "Amazfit", 19999, "Military Rugged 27D", "Military-certified durability for extreme temperatures (-30°C to 70°C), 2000 nits AMOLED display, and 27-day battery life.", "Smartwatches")
]

for name, brand, price, tag, desc, img_key in smartwatch_list:
    add_product(
        name=name,
        brand=brand,
        category="Smartwatches & Wearables",
        subcategory="Smartwatches",
        price=price,
        tag=tag,
        desc=desc,
        features=[
            "High-Resolution Always-On AMOLED / Retina Display with Sapphire Glass",
            "Continuous 24/7 Heart Rate, SpO2, Sleep Tracking & ECG / Blood Oxygen Sensors",
            "Precision Multi-Band Dual-Frequency GPS for Outdoor Navigation & Fitness Tracking",
            "IP68 / 50M - 100M Water-Resistant Aircraft Aluminum / Grade 4 Titanium Bezel"
        ],
        specs={"Display": "AMOLED / Retina Always-On", "Battery Backup": "2 Days to 28 Days", "Sensors": "Heart Rate, SpO2, ECG, Barometer, Compass, GPS", "Waterproof": "5ATM / 10ATM / IP68", "Warranty": "1 Year Brand Warranty"},
        inTheBox="1x Smartwatch with Premium Strap, 1x Magnetic Fast Charging Dock, 1x User Manual & Warranty Seal",
        img_key=img_key,
        warranty="1 Year Brand Warranty",
        compatibleModel="iOS & Android Universal App Sync"
    )

print(f"\n=======================================================")
print(f"Total Products Generated: {len(all_products)}")
cats = {}
for p in all_products:
    c = p['category']
    cats[c] = cats.get(c, 0) + 1
for c, cnt in cats.items():
    print(f" - {c}: {cnt} items")
print(f"=======================================================")

# Output to data.js
js_content = "var products = " + json.dumps(all_products, indent=4) + ";\n\n"
js_content += "if (typeof window !== 'undefined') {\n    window.products = products;\n    window.storeCatalog = products;\n}\n"
js_content += "if (typeof global !== 'undefined') {\n    global.products = products;\n}\n"
js_content += "if (typeof module !== 'undefined' && module.exports) {\n    module.exports = products;\n}\n"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("data.js successfully written!")
