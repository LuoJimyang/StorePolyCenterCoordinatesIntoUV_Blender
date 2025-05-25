import bpy

# 获取当前选中的对象
obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    mesh = obj.data
    
    # 创建新的UV贴图层
    uv_layer_x = mesh.uv_layers.new(name='X_UV')
    uv_layer_y = mesh.uv_layers.new(name='Y_UV')
    uv_layer_z = mesh.uv_layers.new(name='Z_UV')
    
    # 遍历每个面
    for poly in mesh.polygons:
        # 获取面的中心点（本地坐标）
        center = poly.center
        
        # 遍历该面的所有循环（loops）
        for loop_idx in range(poly.loop_start, poly.loop_start + poly.loop_total):
            # 设置X_UV层的U为center.x，V设为0
            uv_layer_x.data[loop_idx].uv = (center.x, 0.0)
            # 设置Y_UV层的U为center.y，V设为0
            uv_layer_y.data[loop_idx].uv = (center.y, 0.0)
            # 设置Z_UV层的U为center.z，V设为0
            uv_layer_z.data[loop_idx].uv = (center.z, 0.0)
    
    # 更新网格数据
    mesh.update()