import gradio as gr
from .unified_pipeline import UnifiedPipeline


def execute_pipeline(file_path: str, dir_path: list[str]):
    paths = []
    if file_path is not None:
        paths += file_path
    if dir_path is not None:
        paths += dir_path
    pipeline = UnifiedPipeline(paths)
    yield from pipeline.execute_pipeline()


def file_upload():
    with gr.Row():
        file_input = gr.File(label="上传文件", file_count="multiple")
        dir_input = gr.File(label="上传目录", file_count="directory")
    progress = gr.HTML(value="<div id='progress-bar'>等待开始...</div>")
    run_btn = gr.Button("开始处理", variant="primary")

    run_btn.click(
        fn=execute_pipeline,
        inputs=[file_input, dir_input],
        outputs=progress,
        queue=True,
    )
