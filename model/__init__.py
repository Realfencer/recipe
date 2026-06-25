from .ralph_base import KarpaBase, KarpaConfig, RalphBase, RalphConfig

# RalphBase/RalphConfig are canonical; KarpaBase/KarpaConfig are back-compat
# aliases retained through the karpa->ralph rebrand (see ralph_base.py).
__all__ = ["RalphBase", "RalphConfig", "KarpaBase", "KarpaConfig"]
self.logit_bias = (
            nn.Parameter(torch.zeros(cfg.vocab_size)) if cfg.use_logit_bias else None
        )