import pathlib

conf_dir = pathlib.Path("/etc/slurm-mail")
conf_file = conf_dir / "slurm-mail.conf"
tpl_dir = conf_dir / "templates"