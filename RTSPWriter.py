import omni
import omni.replicator.core as rep
#from omni.replicator.character.core import RTSPWriter
import omni.replicator.character.core.writers as repchar
from omni.isaac.core.utils.stage import get_current_stage
from omni.isaac.core.utils.prims import get_prim_at_path
from omni.isaac.core.utils.viewports import set_camera_view


# class RTSPWriter(Writer):
#     def __init__(
#         self,
#         output_dir,
#         rgb: bool = True
#     ):
#         self._output_dir = output_dir
#         self.annotators = []
#         if rgb:
#             self.annotators.append(AnnotatorRegistry.get_annotator("rgb"))


# Define the camera path
camera_path = "/World/Carter_v2/chassis_link/camera_mount/carter_camera_stereo_left"

# Get the stage
stage = get_current_stage()

# Get the camera prim
camera_prim = get_prim_at_path(camera_path)

if camera_prim:
    # Set the camera to the active viewport
    viewport = omni.kit.viewport.utility.get_active_viewport()
    viewport.camera_path = camera_path

    # Create a render product
    render_product_path = viewport.render_product_path

    # Initialize the RTSP writer
    #writer = repchar.WriterRegistry.get("RTSPWriter")
    writer=repchar.RTSPWriter()
    writer.initialize()
    

    # Attach the render product to the writer
    writer.attach([render_product_path])

    print(f"Streaming camera from {camera_path} to rtsp://192.168.219.102:8554:8554/RTSPWriter/")

else:
    print(f"Camera prim at {camera_path} not found")
