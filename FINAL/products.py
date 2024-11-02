import base64
import pymongo

# Kết nối tới MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["products_database"]       # Tên database của bạn
collection = db["Healthy Nuts"]           # Tên collection của bạn

# Hàm chuyển đổi một danh sách hình ảnh thành mảng base64
def encode_images(image_files):
    encoded_images = []
    for file in image_files:
        with open(file, "rb") as image_file:
            encoded_images.append(base64.b64encode(image_file.read()).decode('utf-8'))
    return encoded_images
# Chuẩn bị danh sách sản phẩm
products = [
    {
        "name": "Hạt óc chó Mỹ sấy",
        "category": "Healthy Nuts",
        "price": 280000,
        "description": "Nhân hạt óc chó Mỹ sấy - Quả óc chó giàu protein, chất béo có lợi như axit béo omega 3 giúp cải thiện sức khỏe tim mạch, khả năng kiểm soát đường trong máu. Chất béo trong hạt óc chó là chất béo không bão hòa đa, nên lành và tốt cho các chuyển hóa của cơ thể. Ngoài ra, việc sử dụng óc chó khi mang thai sẽ giúp em bé giảm tới 50% các nguy cơ dị tật bẩm sinh, các bệnh về hệ miễn dịch. Hạt óc chó được sấy chín, tách vỏ có thể sử dụng trực tiếp sau khi mua hàng.",
        "images": encode_images([])
    },
    {
        "name": "Hạt Macca Đăk Lăk",
        "category": "Healthy Nuts",
        "price": 480000,
        "description": "Hạt macca có lớp vỏ tròn, màu nâu bóng, phần nhân bên trong vàng ươm. Nhân macca chứa nhiều vitamin, omega-3 và khoáng chất, giúp cải thiện làn da và cung cấp dinh dưỡng cho thai nhi, ngăn ngừa dị tật bẩm sinh. Với hàm lượng dầu cao và axit béo không no, macca giúp giảm cholesterol và hỗ trợ sức khỏe tim mạch. Ngoài ra, chất xơ dồi dào trong nhân macca còn giúp cơ thể trao đổi chất, loại bỏ mỡ thừa.",
        "images": encode_images([])
    },
    {
        "name": "Hạt hạnh nhân Mỹ",
        "category": "Healthy Nuts",
        "price": 69000,
        "description": "Hạt hạnh nhân Mỹ - Hạt hạnh nhân giàu chất xơ, protein, chất béo không bão hòa đơn, vitamin E, magie, và các khoáng chất quan trọng, giúp bảo vệ tế bào, hỗ trợ sức khỏe tim mạch, kiểm soát đường huyết và huyết áp. Với lượng canxi và chất đạm cao, hạnh nhân giúp phát triển xương và trí não, đồng thời tăng cường sức đề kháng. Hạt hạnh nhân cũng là lựa chọn lý tưởng cho người ăn kiêng, giúp no lâu, giảm cân và duy trì sức khỏe tiêu hóa. Hạt hạnh nhân tách vỏ mang trọn hương vị thơm, ngọt bùi tự nhiên nhất bởi 100% nhập khẩu tại Mỹ được đóng gói hút chân không an toàn.",
        "images": encode_images([])
    },
    {
        "name": "Hạt điều rang muối",
        "category": "Healthy Nuts",
        "price": 200000,
        "description": "Hạt điều lụa cung cấp 551 Kcal/100g cùng nhiều dưỡng chất quan trọng giúp giảm cholesterol xấu, hỗ trợ phát triển xương, răng và tăng chiều cao. Chất xơ trong hạt điều giúp no lâu, ngăn ngừa tích tụ mỡ thừa, mang lại vóc dáng cân đối. Ngoài ra, chất chống oxy hóa trong hạt điều còn bảo vệ mắt và da khỏi tác hại của tia UV.",
        "images": encode_images([])
    },
    {
        "name": "Hạt đậu gà Mỹ",
        "category": "Healthy Nuts",
        "price": 89000,
        "description": "Hạt đậu gà Mỹ - Hạt đậu gà giàu đạm, chất xơ, sắt, canxi, và nhiều vitamin thiết yếu giúp kiểm soát cholesterol, ổn định huyết áp, và phòng ngừa tăng huyết áp. Chất xơ và vitamin trong đậu gà còn giúp kiểm soát cơn thèm ăn, hỗ trợ giảm cân mà vẫn đảm bảo đủ dinh dưỡng cho cơ thể. Hạt đậu gà nhập khẩu được phơi khô, hạt nhỏ, cứng căng bóng, không có sâu mọt, khi nấu chín thì nở bung mềm, sẽ có vị thơm bùi ngậy, ngọt nhẹ.",
        "images": encode_images([])
    },
    {
        "name": "Hạt chia Organic Úc",
        "category": "Healthy Nuts",
        "price": 250000,
        "description": "Hạt chia Organic Úc - Hạt Chia Organic Úc giàu omega-3, canxi, kali và magie, giúp bảo vệ sức khỏe, cải thiện da, móng, tóc và hỗ trợ kiểm soát cân nặng. Đây là thực phẩm dinh dưỡng phù hợp cho người ăn kiêng hoặc thiếu chất, mang lại nhiều lợi ích sức khỏe đã được chứng minh qua nghiên cứu. Hạt chia cũng là lựa chọn lý tưởng để bổ sung vào các bữa ăn hàng ngày, giúp duy trì lối sống lành mạnh và cân bằng dinh dưỡng.",
        "images": encode_images([])
    },
    {
        "name": "Hạt bí rang mộc",
        "category": "Healthy Nuts",
        "price": 140000,
        "description": "Hạt bí rang mộc - thơm ngon, vỏ giòn, hạt bùi. Hạt bí chứa tới 50% nhu cầu magie hàng ngày, giúp phân bổ năng lượng, tăng tuần hoàn máu và phòng ngừa bệnh tim, đột quỵ. Hạt bí xanh cũng giàu kẽm và vitamin, hỗ trợ giấc ngủ, cải thiện tâm trạng và nâng cao khả năng miễn dịch. Bổ sung omega-3 từ hạt bí giúp tăng chức năng nhận thức, giảm căng thẳng và đau đầu. Hợp chất L-tryptophan trong hạt bí giúp thư giãn thần kinh, cải thiện giấc ngủ và giảm trầm cảm.",
        "images": encode_images([])
    },
    {
        "name": "Đậu xanh",
        "category": "Healthy Nuts",
        "price": 50000,
        "description": "Đậu xanh - hạt nhỏ bóng, chắc mẩy, khi nấu thì bung mềm, bùi thơm mang tới hương vị đặc trưng cho cho các món ăn chế biến bằng đậu xanh, giúp món ăn trở nên thơm ngon, trọn vị. Đậu xanh giàu dưỡng chất như protein, chất béo, chất xơ, vitamin B1, mangan, sắt, và magie, mang lại nhiều lợi ích cho sức khỏe. Đậu xanh giúp giảm cholesterol xấu, ngăn ngừa các bệnh tim mạch, cao huyết áp và hỗ trợ phòng tránh ung thư nhờ chất chống oxy hóa. Ngoài ra, đậu xanh còn giúp duy trì vóc dáng cân đối, giảm cảm giác thèm ăn và hỗ trợ giảm cân hiệu quả. Trong điều kiện thời tiết mùa hè nắng nóng, khắc nghiệt, việc bổ sung nước đậu xanh rang hay chè đậu xanh, sữa đậu xanh sẽ giúp hạn chế mất nước, ngăn sốc nhiệt. ",
        "images": encode_images([])
    },
    {
        "name": "Đậu đỏ",
        "category": "Healthy Nuts",
        "price": 50000,
        "description": "Đậu đỏ - Đậu đỏ giàu chất chống oxy hóa giúp tăng sức đề kháng, ngăn ngừa vi khuẩn, virus và hỗ trợ tiêu diệt tế bào ung thư. Với hàm lượng kali cao, đậu đỏ giúp kiểm soát huyết áp, ngăn ngừa đột quỵ, đặc biệt ở người cao tuổi. Chất xơ trong đậu đỏ cải thiện tiêu hóa, giúp no lâu và hỗ trợ giảm cân. Ngoài ra, đậu đỏ còn tốt cho gan, thận và có thể dùng làm mặt nạ dưỡng da, giúp da mịn màng, giảm mụn.",
        "images": encode_images([])
    },
    {
        "name": "Táo đỏ",
        "category": "Healthy Nuts",
        "price": 299000,
        "description": "Táo đỏ là nguồn cung cấp dồi dào chất chống oxy hóa, giúp tăng cường hệ miễn dịch và chống lại các gốc tự do, hỗ trợ giảm nguy cơ ung thư. Táo đỏ chứa hàm lượng vitamin C cao, giúp làm đẹp da, chống lão hóa và hỗ trợ sản sinh collagen, làm da săn chắc và mịn màng. Ngoài ra, táo đỏ còn giúp giảm căng thẳng, cải thiện giấc ngủ và tăng cường trí nhớ nhờ các hợp chất flavonoid. Hàm lượng chất xơ trong táo đỏ giúp điều hòa tiêu hóa, giảm cholesterol xấu, hỗ trợ giảm cân và cải thiện sức khỏe tim mạch. Táo đỏ có thể được dùng như một món ăn nhẹ lành mạnh hoặc chế biến trong các món súp, chè, giúp cơ thể thư giãn và phục hồi năng lượng.",
        "images": encode_images([])
    },
    {
        "name": "Nam Việt Quất sấy",
        "category": "Healthy Nuts",
        "price": 250000,
        "description": "Nam Việt Quất sấy - Nam Việt Quất sấy là nguồn giàu chất chống oxy hóa, đặc biệt là polyphenol, giúp ngăn ngừa tổn thương tế bào, hỗ trợ giảm nguy cơ ung thư và các bệnh mãn tính. Chúng chứa vitamin C và E dồi dào, giúp tăng cường hệ miễn dịch, làm đẹp da và chống lại các dấu hiệu lão hóa. Nam Việt Quất sấy cũng nổi tiếng với khả năng hỗ trợ sức khỏe đường tiết niệu, ngăn ngừa nhiễm trùng nhờ hợp chất proanthocyanidins, giúp ngăn chặn vi khuẩn bám vào thành bàng quang. Hàm lượng chất xơ cao trong Nam Việt Quất sấy giúp cải thiện tiêu hóa, duy trì cảm giác no lâu, hỗ trợ giảm cân và kiểm soát cholesterol. Đây là món ăn vặt lành mạnh, có thể dùng riêng hoặc kết hợp trong các món salad, ngũ cốc và sữa chua, giúp bổ sung dinh dưỡng và tăng cường sức khỏe toàn diện.",
        "images": encode_images([])
    },
    {
        "name": "Mixed nuts 8 loại hạt không yến mạch",
        "category": "Healthy Nuts",
        "price": 419000,
        "description": "Sự kết hợp hoàn hảo của 8 loại hạt và trái cây sấy giàu dinh dưỡng, giúp cung cấp nguồn dưỡng chất toàn diện cho mẹ và bé trong suốt thai kỳ. Sản phẩm chứa nhiều vitamin và khoáng chất thiết yếu như Omega-3, vitamin nhóm B, chất xơ và protein, giúp hỗ trợ sự phát triển thể chất và trí não của trẻ.",
        "images": encode_images([])
    },
    {
        "name": "Mix nuts 5 loại hạt Macca, Óc chó, Hạnh nhân, Hạt điều, Hạt bí",
        "category": "Healthy Nuts",
        "price": 350000,
        "description": "Sự kết hợp của hạnh nhân, bí xanh, hạt điều, óc chó và macca mang đến nguồn dưỡng chất phong phú, giàu chất béo lành mạnh, vitamin, tinh bột tốt, chất đạm và chất xơ.",
        "images": encode_images([])
    },
    {
        "name": "Mix nuts 4 loại hạt Macca, Óc chó, Hạnh nhân, Hạt điều",
        "category": "Healthy Nuts",
        "price": 320000,
        "description": "Hỗn hợp dinh dưỡng hoàn hảo gồm Macca, Óc Chó, Hạnh Nhân và Hạt Điều, mang lại nguồn dưỡng chất phong phú cho sức khỏe của mọi lứa tuổi, đặc biệt là mẹ bầu, người già và trẻ nhỏ.",
        "images": encode_images([])
    },
    {
        "name": "Hạt ý dĩ",
        "category": "Healthy Nuts",
        "price": 98000,
        "description": "Hạt ý dĩ, còn được gọi là cườm thảo hay bo bo, là một loại ngũ cốc giàu dinh dưỡng và có nhiều lợi ích cho sức khỏe. Với hàm lượng chất xơ, protein, vitamin và khoáng chất cao, hạt ý dĩ là lựa chọn lý tưởng cho người muốn cải thiện sức khỏe và phòng ngừa bệnh tật.",
        "images": encode_images([])
    },
    {
        "name": "Hạt sen tươi",
        "category": "Healthy Nuts",
        "price": 150000,
        "description": "Hạt sen tươi - Hạt sen từ lâu được sử dụng trong đông y và thực phẩm bổ sung, giúp tăng cường trí não, hỗ trợ điều trị đau đầu, mất ngủ. Hàm lượng glucozit trong hạt sen tươi có tác dụng an thần, giúp ngủ ngon, đặc biệt tốt cho người lớn tuổi. Hạt sen cũng giúp phục hồi sức khỏe sau phẫu thuật, sinh nở, và chứa enzyme tái tạo tế bào, cải thiện da và giảm nếp nhăn. Với nhiều chất xơ và dưỡng chất, hạt sen hỗ trợ thải độc, giảm cân hiệu quả mà không lo tăng cân khi dùng ít đường. Có thể ăn sống trực tiếp sau khi bốc đi phần vỏ.",
        "images": encode_images([])
    },
    {
        "name": "Hạt kiều mạch",
        "category": "Healthy Nuts",
        "price": 55000,
        "description": "Hạt kiều mạch là một loại ngũ cốc không chứa gluten, giàu dinh dưỡng và rất tốt cho sức khỏe. Với hàm lượng cao chất xơ, protein, vitamin và khoáng chất, kiều mạch là lựa chọn tuyệt vời cho người ăn chay, người bị tiểu đường, và những ai muốn duy trì cân nặng và sức khỏe tim mạch.",
        "images": encode_images([])
    },
    {
        "name": "Đậu nành",
        "category": "Healthy Nuts",
        "price": 55000,
        "description": "Hạt đậu nành - Hạt đậu nành giàu dinh dưỡng, chứa protein hoàn chỉnh và có khả năng thay thế protein động vật, giúp giảm cholesterol xấu và ngăn ngừa bệnh tim mạch. Folate trong đậu nành hỗ trợ giảm mệt mỏi, cải thiện tâm trạng, và tăng cường giấc ngủ. Hạt đậu nành còn chứa Genistein, giúp tái tạo tế bào và làm đẹp da. Hạt đậu nành có thể chế biến được nhiều món ăn khác nhau: sữa đậu nành, nấu canh, đậu phụ, chao, miso, sữa hạt,…",
        "images": encode_images([])
    },
    {
        "name": "Mix nuts 5 loại hạt Bí xanh, Hạnh nhân, Macca, Hạt điều, Xoài sấy",
        "category": "Healthy Nuts",
        "price": 290000,
        "description": "Sự lựa chọn tuyệt vời cho bà bầu, người ăn kiêng và những ai muốn duy trì sức khỏe. Hạt bí xanh, hạnh nhân, macca, hạt điều và xoài sấy, được chọn lọc từ vụ mới, đảm bảo tỉ lệ hạt bị lỗi <1%. Sản phẩm được chế biến và đóng gói theo quy trình vệ sinh an toàn thực phẩm, không chứa chất bảo quản và hoàn toàn an toàn cho sức khỏe người dùng.",
        "images": encode_images([])
    },
    {
        "name": "Mix nuts 8 loại hạt và hoa quả sấy",
        "category": "Healthy Nuts",
        "price": 350000,
        "description": "Sản phẩm dinh dưỡng hoàn hảo, đáp ứng mọi nhu cầu dinh dưỡng an toàn và cần thiết cho mẹ bầu và sự phát triển của bé trong suốt thai kỳ. Với sự kết hợp của 8 loại hạt giàu vitamin, khoáng chất, chất béo lành mạnh và chất chống oxy hóa, Hebekery cung cấp giải pháp dinh dưỡng toàn diện từ những nguyên liệu tự nhiên và được chọn lọc kỹ lưỡng.",
        "images": encode_images([])
    },
]

# Lưu tất cả sản phẩm vào MongoDB cùng lúc
collection.insert_many(products)
print("Tất cả sản phẩm đã được lưu vào MongoDB.")