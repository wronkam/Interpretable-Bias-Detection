# Interpretable Bias Detection
Project for *Trustworthy Machine Learning* course at Jagiellonian University.

Contains: 
[**B-cos**](https://github.com/B-cos/B-cos-v2) in [bcos_model directory](/bcos_model)
[**PipNet**](https://github.com/M-Nauta/PIPNet)) in [pipnet_model directory](/pipnet_model)

Intended to be used with *gender biased CelebA* and *WaterBirds* datasets from [B2T](https://github.com/alinlab/b2t).

Dataset can be processed with **prepar_\*.py** script. 
Its placement should be added as arg for pipnet and in [bcos settings file](/bcos_model/bcos/settings.py).

[yml](/TML_environment.yml) file should be used to create the environment. 

Training scripts for both datasets are in associated model subdirectories.

[Checkpoints](https://ujchmura-my.sharepoint.com/:f:/g/personal/michal_wronka_student_uj_edu_pl/EmJijtV__Q9BhGv-aBiHUdoBrJlAPszoTDqw8icyfOrQOQ?e=Xfyzeb) (requires UJ email).

[B-cos wandb page](https://wandb.ai/wronkam/TML_interpretable_bias_detection/) 

---
Issue with Bcos model:

~~~
Traceback (most recent call last):
  File "location/Interpretable-Bias-Detection/bcos_model/train.py", line 153, in <module>
    trainer.run_training(args)
  File "location/Interpretable-Bias-Detection/bcos_model/bcos/training/trainer.py", line 307, in run_training
    trainer.fit(model, datamodule=datamodule, ckpt_path=ckpt_path,)
...
  File "env_location/envs/TML/lib/python3.10/site-packages/pytorch_lightning/plugins/precision/precision.py", line 88, in _after_closure
      self._clip_gradients(
    File "env_location/envs/TML/lib/python3.10/site-packages/pytorch_lightning/plugins/precision/precision.py", line 135, in _clip_gradients
      call._call_lightning_module_hook(
    File "env_location/envs/TML/lib/python3.10/site-packages/pytorch_lightning/trainer/call.py", line 157, in _call_lightning_module_hook
      output = fn(*args, **kwargs)
  TypeError: ClassificationLitModel.configure_gradient_clipping() missing 1 required positional argument: 'optimizer_idx'
~~~
A brute force solution, but nevertheless a viable one, is to edit the following file:
~~~ 
"env_location/envs/TML/lib/python3.10/site-packages/pytorch_lightning/trainer/call.py", line 157, in _call_lightning_module_hook
~~~ 
add `optimizer_idx=0`, as the last argument of `call._call_lightning_module_hook` at the end of the aforementioned method.
