# RoboManipBaselines Setup README

## 環境構築

このプロジェクトをローカルに構築するための手順を説明します。

### 推奨OS

- **Ubuntu 22.04**を強くおすすめします。
- **Ubuntu 20.04**や**Ubuntu 24.04**では、インストール時に問題が発生する可能性があります。

### インストール方法

このプロジェクトは、**pip**または**docker**を使って環境構築することができますが、**docker**を使用する場合、OpenGLのGPUサポート環境構築が複雑であり、**pip**を使ったインストール方法を推奨します。

#### 1. pipを使用する場合

1. 必要なパッケージをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

2. その他の依存関係については、`doc/install.md` を参照し、必要な手順を進めてください。

#### 2. Dockerを使用する場合

- DockerでのセットアップはOpenGLのGPUサポートの環境構築が複雑であり、**推奨しません**。  
  過去に挑戦したが、途中で挫折しました。

### egl_probeのインストール時エラー

インストール中に `egl_probe` のエラーが発生する場合があります。この問題は以下のコマンドで解決できます。

```bash
pip install -e .[diffusion-policy]
```

もしエラーが発生した場合、`cmake`をインストールすることで解決できます。以下のコマンドで`cmake`をインストールしてください。

```bash
sudo apt-get install cmake
```

詳細な解決方法については、[egl_probe Installation Issue](https://github.com/StanfordVL/egl_probe/issues/2) を参照してください。

## その他

- インストール後、プロジェクトを実行するために必要な手順や、サンプルコードについては、`doc`フォルダ内のドキュメントをご覧ください。
- その他の問題が発生した場合は、[Issue Tracker]にて報告してください。



## Train and run
### Diffusion policy
You can see here robo_manip_baselines/diffusion_policy/README.md
#### Dataset preparation
```console
python ../utils/convert_npz_to_zarr.py \
--in_dir ../teleop/teleop_data/TeleopMujocoUR5eParticle_Dataset30_20241031 --out_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031.zarr \
--nproc `nproc` --skip 3
```
a#### Model training
```console
python ./bin/TrainDiffusionPolicy.py \
task.dataset.zarr_path=./data/TeleopMujocoUR5eParticle_Dataset30_20241031.zarr task.name=TeleopMujocoUR5eParticle_Dataset30_20241031
```

```console
$ python ./bin/rollout/RolloutDiffusionPolicyMujocoUR5eParticle.py \
--checkpoint ./log/TeleopMujocoUR5eParticle_Dataset30_20241031_20241226_172951/checkpoints/200.ckpt \
--skip 3 --world_idx 0
```
### SARNN
```console
python ../utils/make_dataset.py \
--in_dir ../teleop/teleop_data/TeleopMujocoUR5eParticle_Dataset30_20241031 --out_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 \
--train_ratio 0.8 --nproc `nproc` --skip 6 --cropped_img_size 280 --resized_img_size 64
```

```console
python ./bin/TrainSarnn.py \
--data_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 --log_dir ./log/TeleopMujocoUR5eParticle_Dataset30_20241031 \
--no_side_image --no_wrench --with_mask
```

```console
python ./bin/rollout/RolloutSarnnMujocoUR5eParticle.py \
--checkpoint ./log/TeleopMujocoUR5eParticle_Dataset30_20241031/20241226_1307_58/SARNN.pth \
--cropped_img_size 280 --skip 6 --world_idx 0
```

### ACT
```console
$ python ../utils/make_dataset.py \
--in_dir ../teleop/teleop_data/TeleopMujocoUR5eParticle_Dataset30_20241031 --out_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 \
--train_ratio 0.8 --nproc `nproc` --skip 3
```

```console
$ python ./bin/TrainAct.py --dataset_dir ./data/TeleopMujocoUR5eParticle_Dataset30_20241031 --log_dir ./log/TeleopMujocoUR5eParticle_Dataset30_20241031
```

```console
$ python ./bin/rollout/RolloutActMujocoUR5eParticle.py \
--checkpoint ./log/TeleopMujocoUR5eParticle_Dataset30_20241031/policy_last.ckpt \
--skip 3 --world_idx 0
```